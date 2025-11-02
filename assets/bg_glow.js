// Veekstar Glow Effect Script
document.addEventListener("mousemove", (e) => {
  const glow = document.createElement("div");
  glow.className = "glow-spot";
  glow.style.left = `${e.pageX}px`;
  glow.style.top = `${e.pageY}px`;
  document.body.appendChild(glow);
  setTimeout(() => glow.remove(), 1000);
});

const style = document.createElement("style");
style.innerHTML = `
  .glow-spot {
    position: absolute;
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, rgba(255,200,0,0.15) 0%, rgba(255,200,0,0) 70%);
    pointer-events: none;
    transform: translate(-50%, -50%);
    animation: fadeOut 1s ease-out forwards;
  }

  @keyframes fadeOut {
    0% { opacity: 1; }
    100% { opacity: 0; }
  }
`;
document.head.appendChild(style);
