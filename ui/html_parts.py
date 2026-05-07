# HTML parts - assembled by build_ui.py
HTML = ""

HTML += """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ritwija — My Personal OS ✦</title>
<link rel="stylesheet" href="style.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
</head>
<body>
<div class="app">

<!-- SIDEBAR -->
<aside class="sidebar" id="sidebar">
  <div class="sidebar-header">
    <div class="logo">
      <span class="logo-icon">✦</span>
      <span class="logo-text">Ritwija OS</span>
    </div>
    <button class="new-chat-btn" id="newChatBtn" title="New Chat">+</button>
  </div>

  <nav class="tab-nav" id="tabNav">
    <button class="tab-btn active" data-tab="chat">💬 Chat</button>
    <button class="tab-btn" data-tab="goals">🎯 Goals</button>
    <button class="tab-btn" data-tab="diary">📔 Diary</button>
    <button class="tab-btn" data-tab="relationships">💞 Relationships</button>
    <button class="tab-btn" data-tab="career">🚀 Career</button>
    <button class="tab-btn" data-tab="fitness">💪 Fitness</button>
    <button class="tab-btn" data-tab="fashion">👗 Fashion</button>
    <button class="tab-btn" data-tab="finances">💰 Finances</button>
  </nav>

  <div class="sidebar-threads" id="chatSidebarSection">
    <div class="section-label">Conversations</div>
    <div class="thread-list" id="threadList"><div class="thread-empty">No conversations yet</div></div>
  </div>

  <div class="sidebar-footer">
    <div class="user-badge">
      <div class="user-avatar">R</div>
      <div>
        <div class="user-name">Ritwija Deep</div>
        <div class="user-role">DevOps @ Zscaler ✦</div>
      </div>
    </div>
  </div>
</aside>

<!-- MAIN -->
<main class="main" id="mainArea">
  <div class="topbar">
    <button class="sidebar-toggle" id="sidebarToggle">☰</button>
    <span class="thread-title" id="threadTitle">Hey Ritwija 👋</span>
    <div class="topbar-actions">
      <button class="icon-btn" id="summaryBtn" title="Memory Summary">🧠</button>
      <button class="icon-btn" id="askMeBtn" title="Ask me something">🎲</button>
    </div>
  </div>

  <!-- ===== TAB PANELS ===== -->

  <!-- CHAT TAB -->
  <div class="tab-panel active" id="tab-chat">
    <div class="chat-wrap">
      <div class="welcome" id="welcomeScreen">
        <div class="welcome-glow"></div>
        <div class="welcome-icon">✦</div>
        <h1 class="welcome-title">Hey Ritwija.</h1>
        <p class="welcome-sub">Your personal OS — built around you, remembers everything, judges nothing.</p>
        <div class="prompt-chips">
          <button class="chip" data-prompt="How am I doing with my CKAD prep this week?">📚 CKAD check-in</button>
          <button class="chip" data-prompt="Give me a motivational push for today">⚡ Motivate me</button>
          <button class="chip" data-prompt="Help me reflect on my relationship with Animesh">💞 Relationship check</button>
          <button class="chip" data-prompt="What should I focus on for my career this month?">🚀 Career focus</button>
          <button class="chip" data-prompt="I want to vent about something">🫂 I need to vent</button>
          <button class="chip" data-prompt="Ask me a deep question about myself">🎲 Surprise me</button>
        </div>
      </div>
      <div class="messages" id="messages" style="display:none"></div>
      <div class="input-area">
        <div class="input-box">
          <textarea id="userInput" placeholder="Talk to Cortex…" rows="1"></textarea>
          <button class="send-btn" id="sendBtn" disabled>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
          </button>
        </div>
        <div class="input-hint">Cortex remembers everything · Shift+Enter for new line</div>
      </div>
    </div>
  </div>

  <!-- GOALS TAB -->
  <div class="tab-panel" id="tab-goals">
    <div class="panel-scroll">
      <div class="panel-header">
        <h2 class="panel-title">🎯 Goals</h2>
        <p class="panel-sub">Daily wins, monthly milestones, and the big picture.</p>
      </div>
      <div class="goals-grid">
        <div class="goal-section">
          <div class="goal-section-header">
            <span class="goal-section-icon">☀️</span>
            <h3>Daily Goals</h3>
            <button class="add-btn" data-goal-type="daily">+ Add</button>
          </div>
          <div class="goal-list" id="dailyGoals"></div>
        </div>
        <div class="goal-section">
          <div class="goal-section-header">
            <span class="goal-section-icon">📅</span>
            <h3>Monthly Goals</h3>
            <button class="add-btn" data-goal-type="monthly">+ Add</button>
          </div>
          <div class="goal-list" id="monthlyGoals"></div>
        </div>
        <div class="goal-section">
          <div class="goal-section-header">
            <span class="goal-section-icon">🌟</span>
            <h3>Long-Term Goals</h3>
            <button class="add-btn" data-goal-type="longterm">+ Add</button>
          </div>
          <div class="goal-list" id="longtermGoals"></div>
        </div>
      </div>
      <div class="ask-cortex-bar">
        <input class="ask-input" id="goalsAskInput" placeholder="Ask Cortex about your goals…">
        <button class="ask-send" data-context="goals">Ask ✦</button>
      </div>
      <div class="cortex-reply" id="goalsReply"></div>
    </div>
  </div>

  <!-- DIARY TAB -->
  <div class="tab-panel" id="tab-diary">
    <div class="panel-scroll">
      <div class="panel-header">
        <h2 class="panel-title">📔 Dear Diary</h2>
        <p class="panel-sub">Three good things. Every day. Because you deserve to notice them.</p>
      </div>
      <div class="diary-controls">
        <input type="date" id="diaryDate" class="date-picker">
        <button class="add-btn" id="newDiaryEntry">+ New Entry</button>
      </div>
      <div class="diary-entries" id="diaryEntries"></div>
      <div class="ask-cortex-bar">
        <input class="ask-input" id="diaryAskInput" placeholder="Reflect with Cortex…">
        <button class="ask-send" data-context="diary">Ask ✦</button>
      </div>
      <div class="cortex-reply" id="diaryReply"></div>
    </div>
  </div>

  <!-- RELATIONSHIPS TAB -->
  <div class="tab-panel" id="tab-relationships">
    <div class="panel-scroll">
      <div class="panel-header">
        <h2 class="panel-title">💞 Relationships</h2>
        <p class="panel-sub">Everyone who matters — and how you show up for them.</p>
      </div>
      <div class="rel-categories">
        <button class="rel-cat-btn active" data-rel="partner">💑 Partner</button>
        <button class="rel-cat-btn" data-rel="family">👨‍👩‍👧 Family</button>
        <button class="rel-cat-btn" data-rel="friends">🫂 Friends</button>
        <button class="rel-cat-btn" data-rel="colleagues">💼 Colleagues</button>
        <button class="rel-cat-btn" data-rel="relatives">🌳 Relatives</button>
        <button class="rel-cat-btn" data-rel="acquaintances">🤝 Acquaintances</button>
      </div>
      <div class="rel-panel" id="relPanel">
        <div class="rel-person-grid" id="relPersonGrid"></div>
      </div>
      <button class="add-btn wide-btn" id="addRelPersonBtn">+ Add Person</button>
      <div class="ask-cortex-bar">
        <input class="ask-input" id="relAskInput" placeholder="Ask Cortex about a relationship…">
        <button class="ask-send" data-context="relationships">Ask ✦</button>
      </div>
      <div class="cortex-reply" id="relReply"></div>
    </div>
  </div>

  <!-- CAREER TAB -->
  <div class="tab-panel" id="tab-career">
    <div class="panel-scroll">
      <div class="panel-header">
        <h2 class="panel-title">🚀 Career</h2>
        <p class="panel-sub">Your journey, your stack, your next move.</p>
      </div>
      <div class="career-sections">
        <div class="career-block">
          <h3 class="career-block-title">📖 Background</h3>
          <div class="timeline" id="careerTimeline">
            <div class="timeline-item"><span class="tl-dot"></span><div class="tl-content"><strong>JUIT, Himachal Pradesh</strong><span class="tl-date">2019–2023</span><p>B.Tech Computer Science Engineering</p></div></div>
            <div class="timeline-item"><span class="tl-dot"></span><div class="tl-content"><strong>IIT Delhi Research Internship</strong><span class="tl-date">2022</span><p>Research work + OnePlus community initiatives</p></div></div>
            <div class="timeline-item"><span class="tl-dot active"></span><div class="tl-content"><strong>Zscaler — DevOps Engineer</strong><span class="tl-date">2023–Present</span><p>GitLab CI/CD · AWS · Python · Networking · US team</p></div></div>
          </div>
        </div>
        <div class="career-block">
          <h3 class="career-block-title">🛠 Tech Stack</h3>
          <div class="tech-grid" id="techGrid">
            <div class="tech-tag know">GitLab CI/CD</div>
            <div class="tech-tag know">Python</div>
            <div class="tech-tag know">AWS (basics)</div>
            <div class="tech-tag know">Networking</div>
            <div class="tech-tag know">Linux</div>
            <div class="tech-tag learning">Kubernetes / CKAD</div>
            <div class="tech-tag learning">AWS SAA</div>
            <div class="tech-tag learning">System Design</div>
            <div class="tech-tag learning">DevOps Advanced</div>
            <div class="tech-tag todo">Docker Advanced</div>
            <div class="tech-tag todo">Terraform</div>
            <div class="tech-tag todo">Observability</div>
          </div>
          <div class="tech-legend"><span class="tech-tag know">Know</span><span class="tech-tag learning">Learning</span><span class="tech-tag todo">Next</span></div>
        </div>
        <div class="career-block">
          <h3 class="career-block-title">📊 LeetCode Journey</h3>
          <div class="lc-stats">
            <div class="lc-stat"><span class="lc-num" id="lcEasy">0</span><span class="lc-label">Easy</span></div>
            <div class="lc-stat"><span class="lc-num" id="lcMedium">0</span><span class="lc-label">Medium</span></div>
            <div class="lc-stat"><span class="lc-num" id="lcHard">0</span><span class="lc-label">Hard</span></div>
          </div>
          <button class="add-btn" id="updateLCBtn">Update Stats</button>
        </div>
        <div class="career-block">
          <h3 class="career-block-title">🌏 Conferences &amp; Events</h3>
          <div class="conf-list" id="confList"></div>
          <button class="add-btn" id="addConfBtn">+ Add Conference</button>
        </div>
        <div class="career-block">
          <h3 class="career-block-title">🤖 AI Updates &amp; Learnings</h3>
          <div class="ai-notes" id="aiNotes"></div>
          <button class="add-btn" id="addAINoteBtn">+ Add Note</button>
        </div>
      </div>
      <div class="ask-cortex-bar">
        <input class="ask-input" id="careerAskInput" placeholder="Ask Cortex about your career…">
        <button class="ask-send" data-context="career">Ask ✦</button>
      </div>
      <div class="cortex-reply" id="careerReply"></div>
    </div>
  </div>

  <!-- FITNESS TAB -->
  <div class="tab-panel" id="tab-fitness">
    <div class="panel-scroll">
      <div class="panel-header">
        <h2 class="panel-title">💪 Fitness</h2>
        <p class="panel-sub">Your body, your energy, your glow-up — tracked with love.</p>
      </div>
      <div class="fitness-grid">
        <div class="fitness-card">
          <h3>💧 Today's Hydration</h3>
          <div class="water-tracker">
            <div class="water-glasses" id="waterGlasses"></div>
            <button class="add-btn" id="addWaterBtn">+ Glass</button>
          </div>
        </div>
        <div class="fitness-card">
          <h3>👟 Step Count</h3>
          <div class="steps-display"><span id="stepCount" class="big-num">0</span><span class="big-unit">steps</span></div>
          <button class="add-btn" id="updateStepsBtn">Update</button>
        </div>
        <div class="fitness-card">
          <h3>🔥 BMR &amp; Calories</h3>
          <div class="bmr-info" id="bmrInfo">
            <div class="bmr-row"><span>BMR</span><span id="bmrVal">~1,450 kcal</span></div>
            <div class="bmr-row"><span>Goal</span><span id="bmrGoal">Maintenance</span></div>
          </div>
          <button class="add-btn" id="editBMRBtn">Edit</button>
        </div>
        <div class="fitness-card">
          <h3>🏋️ Gym Log</h3>
          <div class="gym-log" id="gymLog"></div>
          <button class="add-btn" id="addGymBtn">+ Log Workout</button>
        </div>
        <div class="fitness-card">
          <h3>🍽 Food &amp; Patterns</h3>
          <div class="food-log" id="foodLog"></div>
          <button class="add-btn" id="addFoodBtn">+ Log Meal</button>
        </div>
        <div class="fitness-card">
          <h3>✨ Skin &amp; Hair Care</h3>
          <div class="skin-log" id="skinLog"></div>
          <button class="add-btn" id="addSkinBtn">+ Log Check-in</button>
        </div>
        <div class="fitness-card wide-card">
          <h3>🎯 Focus Areas</h3>
          <div class="focus-tags">
            <span class="focus-tag">Face fat reduction</span>
            <span class="focus-tag">Clean teeth routine</span>
            <span class="focus-tag">Hair care</span>
            <span class="focus-tag">Try a sport / dance</span>
            <span class="focus-tag">Consistent gym</span>
          </div>
        </div>
      </div>
      <div class="ask-cortex-bar">
        <input class="ask-input" id="fitnessAskInput" placeholder="Ask Cortex about fitness…">
        <button class="ask-send" data-context="fitness">Ask ✦</button>
      </div>
      <div class="cortex-reply" id="fitnessReply"></div>
    </div>
  </div>

  <!-- FASHION TAB -->
  <div class="tab-panel" id="tab-fashion">
    <div class="panel-scroll">
      <div class="panel-header">
        <h2 class="panel-title">👗 Fashion Stylist</h2>
        <p class="panel-sub">Warm undertone · Pear-shaped · Main character energy. Always.</p>
      </div>
      <div class="fashion-categories">
        <button class="fashion-cat-btn active" data-fashion="office">💼 Office</button>
        <button class="fashion-cat-btn" data-fashion="casual">☕ Casual</button>
        <button class="fashion-cat-btn" data-fashion="nightout">🌙 Night Out</button>
        <button class="fashion-cat-btn" data-fashion="party">🎉 Party/Wedding</button>
        <button class="fashion-cat-btn" data-fashion="traditional">🪷 Traditional</button>
      </div>
      <div class="fashion-panel" id="fashionPanel">
        <div class="fashion-tips" id="fashionTips"></div>
        <button class="add-btn" id="addFashionItemBtn">+ Add Outfit / Note</button>
      </div>
      <div class="body-profile-card">
        <h3>👤 Your Style Profile</h3>
        <div class="body-profile-grid">
          <div class="bp-item"><span class="bp-label">Undertone</span><span class="bp-val">Warm 🌻</span></div>
          <div class="bp-item"><span class="bp-label">Body Shape</span><span class="bp-val">Pear 🍐</span></div>
          <div class="bp-item"><span class="bp-label">Vibe</span><span class="bp-val">Elegant + Comfy</span></div>
          <div class="bp-item"><span class="bp-label">Colors</span><span class="bp-val">Earthy, Rust, Olive, Cream</span></div>
        </div>
      </div>
      <div class="ask-cortex-bar">
        <input class="ask-input" id="fashionAskInput" placeholder="Ask Cortex for outfit advice…">
        <button class="ask-send" data-context="fashion">Ask ✦</button>
      </div>
      <div class="cortex-reply" id="fashionReply"></div>
    </div>
  </div>

  <!-- FINANCES TAB -->
  <div class="tab-panel" id="tab-finances">
    <div class="panel-scroll">
      <div class="panel-header">
        <h2 class="panel-title">💰 Finances</h2>
        <p class="panel-sub">Money sorted. Future secured. Mumma taken care of.</p>
      </div>
      <div class="finance-grid">
        <div class="finance-card">
          <h3>📊 Monthly Overview</h3>
          <div class="finance-row"><span>Income</span><span class="finance-val green" id="finIncome">₹ —</span></div>
          <div class="finance-row"><span>Expenses</span><span class="finance-val red" id="finExpenses">₹ —</span></div>
          <div class="finance-row"><span>Savings</span><span class="finance-val green" id="finSavings">₹ —</span></div>
          <button class="add-btn" id="editFinanceBtn">Edit</button>
        </div>
        <div class="finance-card">
          <h3>🎯 Savings Goals</h3>
          <div class="savings-goals" id="savingsGoals"></div>
          <button class="add-btn" id="addSavingsGoalBtn">+ Add Goal</button>
        </div>
        <div class="finance-card">
          <h3>📝 Expense Log</h3>
          <div class="expense-log" id="expenseLog"></div>
          <button class="add-btn" id="addExpenseBtn">+ Add Expense</button>
        </div>
        <div class="finance-card">
          <h3>💡 Finance Notes</h3>
          <div class="finance-notes" id="financeNotes"></div>
          <button class="add-btn" id="addFinanceNoteBtn">+ Add Note</button>
        </div>
      </div>
      <div class="ask-cortex-bar">
        <input class="ask-input" id="financeAskInput" placeholder="Ask Cortex about finances…">
        <button class="ask-send" data-context="finances">Ask ✦</button>
      </div>
      <div class="cortex-reply" id="financeReply"></div>
    </div>
  </div>

</main>

<!-- ===== MODALS ===== -->
<div class="modal-overlay" id="summaryModal" style="display:none">
  <div class="modal">
    <div class="modal-header"><h2>🧠 Memory Summary</h2><button class="modal-close" id="closeSummaryModal">✕</button></div>
    <div class="modal-desc">What Cortex remembers about this conversation.</div>
    <div class="summary-content" id="summaryContent"><div class="summary-loading">Loading…</div></div>
    <div class="modal-actions"><button class="btn-secondary" id="closeSummaryModal2">Close</button></div>
  </div>
</div>

<div class="modal-overlay" id="genericModal" style="display:none">
  <div class="modal">
    <div class="modal-header"><h2 id="genericModalTitle">Add</h2><button class="modal-close" id="closeGenericModal">✕</button></div>
    <textarea class="modal-textarea" id="genericModalInput" rows="4" placeholder="Type here…"></textarea>
    <div class="modal-actions">
      <button class="btn-secondary" id="cancelGenericModal">Cancel</button>
      <button class="btn-primary" id="saveGenericModal">Save ✦</button>
    </div>
  </div>
</div>

<div class="modal-overlay" id="askModal" style="display:none">
  <div class="modal">
    <div class="modal-header"><h2>🎲 Cortex asks you…</h2><button class="modal-close" id="closeAskModal">✕</button></div>
    <p class="modal-desc" id="askModalQuestion"></p>
    <textarea class="modal-textarea" id="askModalAnswer" rows="4" placeholder="Your answer…"></textarea>
    <div class="modal-actions">
      <button class="btn-secondary" id="cancelAskModal">Skip</button>
      <button class="btn-primary" id="sendAskModal">Send to Cortex ✦</button>
    </div>
  </div>
</div>

</div><!-- .app -->
<script src="app.js"></script>
</body>
</html>"""

