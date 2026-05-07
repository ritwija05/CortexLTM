# CSS parts - assembled by build_ui.py
CSS = ""
CSS += """
/* ===== MAIN ===== */
.main{flex:1;display:flex;flex-direction:column;overflow:hidden;background:#0a0a0d}
.topbar{display:flex;align-items:center;gap:12px;padding:12px 20px;border-bottom:1px solid #141420;background:#0a0a0d}
.sidebar-toggle{background:none;border:none;color:#555;font-size:18px;cursor:pointer;padding:4px;border-radius:6px;transition:color .15s}
.sidebar-toggle:hover{color:#aaa}
.thread-title{flex:1;font-size:13px;font-weight:500;color:#666;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topbar-actions{display:flex;gap:8px}
.icon-btn{background:none;border:1px solid #1e1e2a;border-radius:8px;color:#555;font-size:15px;cursor:pointer;padding:6px 10px;transition:all .15s}
.icon-btn:hover{border-color:#e879a0;color:#e879a0;background:#1a0e1c}

/* ===== TAB PANELS ===== */
.tab-panel{display:none;flex:1;overflow:hidden}
.tab-panel.active{display:flex;flex-direction:column}
.panel-scroll{flex:1;overflow-y:auto;padding:28px 32px 40px;max-width:980px;width:100%;margin:0 auto}
.panel-header{margin-bottom:24px}
.panel-title{font-size:26px;font-weight:800;color:#fff;letter-spacing:-.5px}
.panel-sub{font-size:14px;color:#555;margin-top:6px;line-height:1.5}

/* ===== CHAT TAB ===== */
.chat-wrap{display:flex;flex-direction:column;flex:1;overflow:hidden}
.welcome{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px 24px;text-align:center;position:relative;overflow:hidden}
.welcome-glow{position:absolute;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,#e879a018 0%,transparent 70%);top:50%;left:50%;transform:translate(-50%,-60%);pointer-events:none}
.welcome-icon{font-size:48px;margin-bottom:16px;filter:drop-shadow(0 0 20px #e879a088)}
.welcome-title{font-family:'Playfair Display',serif;font-size:42px;font-weight:700;color:#fff;letter-spacing:-.5px;margin-bottom:10px}
.welcome-sub{font-size:15px;color:#555;max-width:400px;line-height:1.6;margin-bottom:32px}
.prompt-chips{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;max-width:580px}
.chip{padding:9px 16px;border-radius:20px;border:1px solid #1e1e2a;background:#0f0f14;color:#999;font-size:13px;cursor:pointer;transition:all .2s;font-family:inherit}
.chip:hover{border-color:#e879a0;color:#e879a0;background:#1a0e1c;transform:translateY(-2px)}

/* ===== MESSAGES ===== */
.messages{flex:1;overflow-y:auto;padding:20px 0;scroll-behavior:smooth}
.message{display:flex;gap:12px;padding:8px 24px;max-width:800px;margin:0 auto;width:100%}
.message.user{flex-direction:row-reverse}
.msg-avatar{width:30px;height:30px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;margin-top:2px}
.message.assistant .msg-avatar{background:linear-gradient(135deg,#e879a0,#f9a8d4);color:#fff}
.message.user .msg-avatar{background:#1e1e2a;color:#888}
.msg-body{max-width:78%}
.msg-name{font-size:10px;font-weight:700;color:#444;margin-bottom:4px;text-transform:uppercase;letter-spacing:.5px}
.message.user .msg-name{text-align:right}
.msg-bubble{padding:11px 15px;border-radius:14px;font-size:14px;line-height:1.65}
.message.assistant .msg-bubble{background:#111118;color:#ddd;border-radius:4px 14px 14px 14px;border:1px solid #1a1a24}
.message.user .msg-bubble{background:#1e1020;color:#f9a8d4;border-radius:14px 4px 14px 14px}
.msg-bubble p{margin-bottom:8px}.msg-bubble p:last-child{margin-bottom:0}
.msg-bubble code{background:#0a0a0d;padding:2px 5px;border-radius:4px;font-family:'SF Mono',monospace;font-size:12px;color:#e879a0}
.msg-bubble pre{background:#0a0a0d;padding:12px;border-radius:8px;overflow-x:auto;margin:8px 0;border:1px solid #1a1a24}
.msg-bubble pre code{background:none;padding:0;color:#f9a8d4}
.typing-indicator{display:flex;gap:4px;align-items:center;padding:12px 15px}
.typing-dot{width:6px;height:6px;border-radius:50%;background:#444;animation:bounce 1.2s infinite}
.typing-dot:nth-child(2){animation-delay:.2s}.typing-dot:nth-child(3){animation-delay:.4s}
@keyframes bounce{0%,60%,100%{transform:translateY(0)}30%{transform:translateY(-5px);background:#e879a0}}

/* ===== INPUT AREA ===== */
.input-area{padding:14px 20px 18px;border-top:1px solid #141420;background:#0a0a0d}
.input-box{display:flex;align-items:flex-end;gap:10px;background:#0f0f14;border:1px solid #1e1e2a;border-radius:12px;padding:9px 9px 9px 14px;transition:border-color .2s}
.input-box:focus-within{border-color:#e879a0}
#userInput{flex:1;background:none;border:none;outline:none;color:#e8e8ed;font-size:14px;line-height:1.5;resize:none;max-height:140px;font-family:inherit}
#userInput::placeholder{color:#333}
.send-btn{width:34px;height:34px;border-radius:9px;border:none;background:#e879a0;color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:all .15s}
.send-btn:disabled{background:#1e1e2a;color:#333;cursor:not-allowed}
.send-btn:not(:disabled):hover{background:#d4608a;transform:scale(1.05)}
.send-btn svg{width:15px;height:15px}
.input-hint{font-size:11px;color:#2a2a38;text-align:center;margin-top:7px}
"""