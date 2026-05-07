css = """/* ===== RESET & BASE ===== */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0d0d0f; color: #e8e8ed; }
.app { display: flex; height: 100vh; overflow: hidden; }

/* ===== SIDEBAR ===== */
.sidebar { width: 260px; min-width: 260px; background: #111114; border-right: 1px solid #1e1e24; display: flex; flex-direction: column; transition: transform 0.25s ease; }
.sidebar-header { display: flex; align-items: center; justify-content: space-between; padding: 18px 16px 14px; border-bottom: 1px solid #1e1e24; }
.logo { display: flex; align-items: center; gap: 8px; }
.logo-icon { font-size: 22px; color: #7c6af7; }
.logo-text { font-size: 17px; font-weight: 700; letter-spacing: -0.3px; color: #fff; }
.new-chat-btn { width: 30px; height: 30px; border-radius: 8px; border: 1px solid #2a2a32; background: #1a1a20; color: #aaa; font-size: 20px; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.15s; }
.new-chat-btn:hover { background: #7c6af7; color: #fff; border-color: #7c6af7; }
.sidebar-section { padding: 14px 12px 8px; flex: 1; overflow-y: auto; }
.sidebar-section + .sidebar-section { border-top: 1px solid #1e1e24; flex: 0; }
.section-label { font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; color: #555; margin-bottom: 8px; padding: 0 4px; }
.thread-list { display: flex; flex-direction: column; gap: 2px; }
.thread-empty { font-size: 12px; color: #444; padding: 8px 4px; }
.thread-item { padding: 8px 10px; border-radius: 8px; cursor: pointer; font-size: 13px; color: #aaa; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; transition: all 0.15s; }
.thread-item:hover { background: #1a1a22; color: #ddd; }
.thread-item.active { background: #1e1b38; color: #a89cf7; }
.story-btn { width: 100%; padding: 8px 10px; border-radius: 8px; border: 1px dashed #2a2a38; background: transparent; color: #7c6af7; font-size: 12px; cursor: pointer; text-align: left; transition: all 0.15s; margin-bottom: 8px; }
.story-btn:hover { background: #1a1a28; border-color: #7c6af7; }
.story-list { display: flex; flex-direction: column; gap: 4px; }
.story-item { padding: 6px 10px; border-radius: 6px; font-size: 12px; color: #888; background: #161618; border-left: 2px solid #7c6af7; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.sidebar-footer { padding: 12px 16px; border-top: 1px solid #1e1e24; }
.user-badge { display: flex; align-items: center; gap: 10px; }
.user-avatar { width: 30px; height: 30px; border-radius: 50%; background: linear-gradient(135deg, #7c6af7, #a78bfa); display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; color: #fff; flex-shrink: 0; }
.user-name { font-size: 13px; color: #bbb; }

/* ===== MAIN ===== */
.main { flex: 1; display: flex; flex-direction: column; overflow: hidden; background: #0d0d0f; }
.topbar { display: flex; align-items: center; gap: 12px; padding: 14px 20px; border-bottom: 1px solid #1a1a20; background: #0d0d0f; }
.sidebar-toggle { background: none; border: none; color: #666; font-size: 18px; cursor: pointer; padding: 4px; border-radius: 6px; transition: color 0.15s; }
.sidebar-toggle:hover { color: #aaa; }
.thread-title { flex: 1; font-size: 14px; font-weight: 500; color: #888; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.topbar-actions { display: flex; gap: 8px; }
.icon-btn { background: none; border: 1px solid #222; border-radius: 8px; color: #666; font-size: 16px; cursor: pointer; padding: 6px 10px; transition: all 0.15s; }
.icon-btn:hover { border-color: #7c6af7; color: #a89cf7; background: #1a1a28; }

/* ===== WELCOME ===== */
.welcome { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px 24px; text-align: center; }
.welcome-icon { font-size: 52px; margin-bottom: 20px; color: #7c6af7; }
.welcome-title { font-size: 32px; font-weight: 700; letter-spacing: -0.5px; color: #fff; margin-bottom: 12px; }
.welcome-sub { font-size: 15px; color: #666; max-width: 420px; line-height: 1.6; margin-bottom: 36px; }
.prompt-chips { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; max-width: 560px; }
.chip { padding: 10px 16px; border-radius: 20px; border: 1px solid #222; background: #111114; color: #bbb; font-size: 13px; cursor: pointer; transition: all 0.2s; }
.chip:hover { border-color: #7c6af7; color: #a89cf7; background: #1a1a28; transform: translateY(-1px); }

/* ===== MESSAGES ===== */
.messages { flex: 1; overflow-y: auto; padding: 24px 0; scroll-behavior: smooth; }
.messages::-webkit-scrollbar { width: 4px; }
.messages::-webkit-scrollbar-track { background: transparent; }
.messages::-webkit-scrollbar-thumb { background: #2a2a32; border-radius: 4px; }
.message { display: flex; gap: 14px; padding: 10px 24px; max-width: 820px; margin: 0 auto; width: 100%; }
.message.user { flex-direction: row-reverse; }
.msg-avatar { width: 32px; height: 32px; border-radius: 50%; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 700; margin-top: 2px; }
.message.assistant .msg-avatar { background: linear-gradient(135deg, #7c6af7, #a78bfa); color: #fff; }
.message.user .msg-avatar { background: linear-gradient(135deg, #2a2a3a, #3a3a4a); color: #aaa; }
.msg-body { max-width: 75%; }
.msg-name { font-size: 11px; font-weight: 600; color: #555; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.5px; }
.message.user .msg-name { text-align: right; }
.msg-bubble { padding: 12px 16px; border-radius: 16px; font-size: 14px; line-height: 1.65; }
.message.assistant .msg-bubble { background: #161618; color: #ddd; border-radius: 4px 16px 16px 16px; }
.message.user .msg-bubble { background: #1e1b38; color: #c4b8ff; border-radius: 16px 4px 16px 16px; }
.msg-bubble p { margin-bottom: 8px; }
.msg-bubble p:last-child { margin-bottom: 0; }
.msg-bubble code { background: #0d0d0f; padding: 2px 6px; border-radius: 4px; font-family: 'SF Mono', monospace; font-size: 12px; color: #a78bfa; }
.msg-bubble pre { background: #0d0d0f; padding: 12px; border-radius: 8px; overflow-x: auto; margin: 8px 0; }
.msg-bubble pre code { background: none; padding: 0; color: #c4b8ff; }
.typing-indicator { display: flex; gap: 4px; align-items: center; padding: 14px 16px; }
.typing-dot { width: 7px; height: 7px; border-radius: 50%; background: #555; animation: bounce 1.2s infinite; }
.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }
@keyframes bounce { 0%, 60%, 100% { transform: translateY(0); } 30% { transform: translateY(-6px); background: #7c6af7; } }

/* ===== INPUT AREA ===== */
.input-area { padding: 16px 24px 20px; border-top: 1px solid #1a1a20; background: #0d0d0f; }
.input-box { display: flex; align-items: flex-end; gap: 10px; background: #111114; border: 1px solid #222; border-radius: 14px; padding: 10px 10px 10px 16px; transition: border-color 0.2s; }
.input-box:focus-within { border-color: #7c6af7; }
#userInput { flex: 1; background: none; border: none; outline: none; color: #e8e8ed; font-size: 14px; line-height: 1.5; resize: none; max-height: 160px; font-family: inherit; }
#userInput::placeholder { color: #444; }
.send-btn { width: 36px; height: 36px; border-radius: 10px; border: none; background: #7c6af7; color: #fff; cursor: pointer; display: flex; align-items: center; justify-content: center; flex-shrink: 0; transition: all 0.15s; }
.send-btn:disabled { background: #222; color: #444; cursor: not-allowed; }
.send-btn:not(:disabled):hover { background: #6b5ce7; transform: scale(1.05); }
.send-btn svg { width: 16px; height: 16px; }
.input-hint { font-size: 11px; color: #333; text-align: center; margin-top: 8px; }

/* ===== MODALS ===== */
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.7); display: flex; align-items: center; justify-content: center; z-index: 100; backdrop-filter: blur(4px); }
.modal { background: #111114; border: 1px solid #222; border-radius: 16px; padding: 28px; width: 90%; max-width: 500px; }
.modal-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; }
.modal-header h2 { font-size: 18px; font-weight: 700; color: #fff; }
.modal-close { background: none; border: none; color: #555; font-size: 18px; cursor: pointer; padding: 4px; border-radius: 6px; transition: color 0.15s; }
.modal-close:hover { color: #aaa; }
.modal-desc { font-size: 13px; color: #666; line-height: 1.6; margin-bottom: 16px; }
.modal-textarea { width: 100%; background: #0d0d0f; border: 1px solid #222; border-radius: 10px; color: #ddd; font-size: 13px; font-family: inherit; padding: 12px; resize: vertical; outline: none; line-height: 1.6; }
.modal-textarea:focus { border-color: #7c6af7; }
.modal-actions { display: flex; gap: 10px; justify-content: flex-end; margin-top: 16px; }
.btn-primary { padding: 9px 20px; border-radius: 9px; border: none; background: #7c6af7; color: #fff; font-size: 13px; font-weight: 600; cursor: pointer; transition: background 0.15s; }
.btn-primary:hover { background: #6b5ce7; }
.btn-secondary { padding: 9px 20px; border-radius: 9px; border: 1px solid #2a2a32; background: transparent; color: #888; font-size: 13px; cursor: pointer; transition: all 0.15s; }
.btn-secondary:hover { border-color: #444; color: #bbb; }
.summary-content { font-size: 13px; color: #bbb; line-height: 1.8; max-height: 400px; overflow-y: auto; }
.summary-loading { color: #555; font-style: italic; }
.summary-content ul { padding-left: 18px; }
.summary-content li { margin-bottom: 6px; }

/* ===== RESPONSIVE ===== */
@media (max-width: 640px) {
  .sidebar { position: fixed; left: 0; top: 0; bottom: 0; z-index: 50; transform: translateX(-100%); }
  .sidebar.open { transform: translateX(0); }
  .welcome-title { font-size: 24px; }
  .message { padding: 8px 14px; }
}
"""
with open('/Users/ritwijadeep/Desktop/CortexLTMFork/CortexLTM/ui/style.css', 'w') as f:
    f.write(css)
print('done')
