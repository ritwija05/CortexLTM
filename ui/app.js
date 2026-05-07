
const API = 'http://localhost:8000';
const USER_ID = '00000000-0000-0000-0000-000000000000';

let currentThreadId = null;
let threads = [];
let stories = JSON.parse(localStorage.getItem('cortex_stories') || '[]');

// DOM refs
const threadList = document.getElementById('threadList');
const messages = document.getElementById('messages');
const welcomeScreen = document.getElementById('welcomeScreen');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const threadTitle = document.getElementById('threadTitle');
const newChatBtn = document.getElementById('newChatBtn');
const sidebarToggle = document.getElementById('sidebarToggle');
const sidebar = document.getElementById('sidebar');
const summaryBtn = document.getElementById('summaryBtn');
const storyList = document.getElementById('storyList');
const addStoryBtn = document.getElementById('addStoryBtn');

// ===== INIT =====
async function init() {
  renderStories();
  await loadThreads();
  setupInput();
  setupChips();
  setupModals();
}

// ===== THREADS =====
async function loadThreads() {
  try {
    const res = await fetch(`${API}/v1/threads?user_id=${USER_ID}&limit=50`);
    if (!res.ok) return;
    const data = await res.json();
    threads = data.threads || [];
    renderThreadList();
  } catch (e) { console.warn('Could not load threads', e); }
}

function renderThreadList() {
  if (!threads.length) {
    threadList.innerHTML = '<div class="thread-empty">No conversations yet</div>';
    return;
  }
  threadList.innerHTML = threads.map(t => `
    <div class="thread-item ${t.id === currentThreadId ? 'active' : ''}"
         data-id="${t.id}" title="${t.title || 'Untitled'}">
      ${t.title || 'Untitled conversation'}
    </div>
  `).join('');
  threadList.querySelectorAll('.thread-item').forEach(el => {
    el.addEventListener('click', () => openThread(el.dataset.id));
  });
}

async function createThread(title) {
  const res = await fetch(`${API}/v1/threads`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ user_id: USER_ID, title: title || 'New conversation' })
  });
  const data = await res.json();
  return data.thread_id;
}

async function openThread(threadId) {
  currentThreadId = threadId;
  const t = threads.find(x => x.id === threadId);
  threadTitle.textContent = t ? (t.title || 'Conversation') : 'Conversation';
  welcomeScreen.style.display = 'none';
  messages.style.display = 'block';
  messages.innerHTML = '';
  renderThreadList();
  await loadMessages(threadId);
}

async function loadMessages(threadId) {
  try {
    const res = await fetch(`${API}/v1/threads/${threadId}/events?limit=100`);
    if (!res.ok) return;
    const data = await res.json();
    (data.messages || []).forEach(m => appendMessage(m.role, m.content, false));
    scrollToBottom();
  } catch (e) { console.warn('Could not load messages', e); }
}

// ===== CHAT =====
async function sendMessage(text) {
  if (!text.trim()) return;

  if (!currentThreadId) {
    const title = text.slice(0, 50) + (text.length > 50 ? '…' : '');
    currentThreadId = await createThread(title);
    welcomeScreen.style.display = 'none';
    messages.style.display = 'block';
    messages.innerHTML = '';
    threadTitle.textContent = title;
    await loadThreads();
    renderThreadList();
  }

  appendMessage('user', text);
  userInput.value = '';
  userInput.style.height = 'auto';
  sendBtn.disabled = true;

  const typingEl = appendTyping();

  try {
    const res = await fetch(`${API}/v1/threads/${currentThreadId}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, short_term_limit: 30 })
    });
    typingEl.remove();
    if (res.ok) {
      const reply = await res.text();
      appendMessage('assistant', reply);
    } else {
      appendMessage('assistant', 'Something went wrong. Please try again.');
    }
  } catch (e) {
    typingEl.remove();
    appendMessage('assistant', 'Could not reach Cortex. Is the server running?');
  }
  scrollToBottom();
}

// ===== RENDER MESSAGES =====
function appendMessage(role, content, scroll = true) {
  const div = document.createElement('div');
  div.className = `message ${role}`;
  const avatar = role === 'assistant' ? '⬡' : 'R';
  const name = role === 'assistant' ? 'Cortex' : 'You';
  div.innerHTML = `
    <div class="msg-avatar">${avatar}</div>
    <div class="msg-body">
      <div class="msg-name">${name}</div>
      <div class="msg-bubble">${formatText(content)}</div>
    </div>
  `;
  messages.appendChild(div);
  if (scroll) scrollToBottom();
  return div;
}

function appendTyping() {
  const div = document.createElement('div');
  div.className = 'message assistant';
  div.innerHTML = `
    <div class="msg-avatar">⬡</div>
    <div class="msg-body">
      <div class="msg-name">Cortex</div>
      <div class="msg-bubble">
        <div class="typing-indicator">
          <div class="typing-dot"></div>
          <div class="typing-dot"></div>
          <div class="typing-dot"></div>
        </div>
      </div>
    </div>
  `;
  messages.appendChild(div);
  scrollToBottom();
  return div;
}

function formatText(text) {
  // basic markdown-ish formatting
  return text
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/\n/g, '<br>');
}

function scrollToBottom() {
  messages.scrollTop = messages.scrollHeight;
}

// ===== INPUT =====
function setupInput() {
  userInput.addEventListener('input', () => {
    sendBtn.disabled = !userInput.value.trim();
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, 160) + 'px';
  });
  userInput.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      if (!sendBtn.disabled) sendMessage(userInput.value.trim());
    }
  });
  sendBtn.addEventListener('click', () => sendMessage(userInput.value.trim()));
  newChatBtn.addEventListener('click', startNewChat);
  sidebarToggle.addEventListener('click', () => sidebar.classList.toggle('open'));
}

function startNewChat() {
  currentThreadId = null;
  messages.innerHTML = '';
  messages.style.display = 'none';
  welcomeScreen.style.display = 'flex';
  threadTitle.textContent = 'Start a conversation';
  renderThreadList();
}

// ===== CHIPS =====
function setupChips() {
  document.querySelectorAll('.chip').forEach(chip => {
    chip.addEventListener('click', () => {
      userInput.value = chip.dataset.prompt;
      sendBtn.disabled = false;
      userInput.focus();
      sendMessage(chip.dataset.prompt);
    });
  });
}

// ===== STORIES =====
function renderStories() {
  if (!stories.length) { storyList.innerHTML = ''; return; }
  storyList.innerHTML = stories.map((s, i) => `
    <div class="story-item" title="${s}">${s.slice(0, 60)}${s.length > 60 ? '…' : ''}</div>
  `).join('');
}

async function saveStory(text) {
  stories.unshift(text);
  localStorage.setItem('cortex_stories', JSON.stringify(stories));
  renderStories();

  // Send story to Cortex as a message so it gets remembered
  if (!currentThreadId) {
    currentThreadId = await createThread('Life Story');
    welcomeScreen.style.display = 'none';
    messages.style.display = 'block';
    messages.innerHTML = '';
    threadTitle.textContent = 'Life Story';
    await loadThreads();
    renderThreadList();
  }
  await sendMessage('I want to share something about myself: ' + text);
}

// ===== MODALS =====
function setupModals() {
  // Story modal
  addStoryBtn.addEventListener('click', () => {
    document.getElementById('storyModal').style.display = 'flex';
    document.getElementById('storyInput').value = '';
    document.getElementById('storyInput').focus();
  });
  document.getElementById('closeStoryModal').addEventListener('click', () => {
    document.getElementById('storyModal').style.display = 'none';
  });
  document.getElementById('cancelStoryBtn').addEventListener('click', () => {
    document.getElementById('storyModal').style.display = 'none';
  });
  document.getElementById('saveStoryBtn').addEventListener('click', async () => {
    const text = document.getElementById('storyInput').value.trim();
    if (!text) return;
    document.getElementById('storyModal').style.display = 'none';
    await saveStory(text);
  });

  // Summary modal
  summaryBtn.addEventListener('click', async () => {
    document.getElementById('summaryModal').style.display = 'flex';
    const content = document.getElementById('summaryContent');
    content.innerHTML = '<div class="summary-loading">Loading memory…</div>';
    if (!currentThreadId) {
      content.innerHTML = '<div class="summary-loading">Start a conversation first.</div>';
      return;
    }
    try {
      const res = await fetch(`${API}/v1/threads/${currentThreadId}/summary`);
      const data = await res.json();
      const summary = data.summary;
      if (summary) {
        const lines = summary.split('\n').filter(Boolean);
        content.innerHTML = '<ul>' + lines.map(l => `<li>${l.replace(/^[-•*]\s*/, '')}</li>`).join('') + '</ul>';
      } else {
        content.innerHTML = '<div class="summary-loading">No memory summary yet — keep chatting!</div>';
      }
    } catch (e) {
      content.innerHTML = '<div class="summary-loading">Could not load summary.</div>';
    }
  });
  document.getElementById('closeSummaryModal').addEventListener('click', () => {
    document.getElementById('summaryModal').style.display = 'none';
  });

  // Close modals on overlay click
  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', e => {
      if (e.target === overlay) overlay.style.display = 'none';
    });
  });
}

init();
