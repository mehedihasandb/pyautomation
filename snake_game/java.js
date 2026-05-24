// 1. Neon effect
function drawSnake() {
  snake.forEach((segment, index) => {
    // Gradient from head to tail
    const alpha = 1 - (index / snake.length) * 0.7;
    ctx.shadowBlur = 20;
    ctx.shadowColor = `rgba(0, 255, 0, ${alpha})`;
    ctx.fillStyle = `rgba(0, 255, 0, ${alpha})`;
    ctx.fillRect(segment.x, segment.y, gridSize, gridSize);
  });
}

// 2. Particle trail
let particles = [];
function updateParticles() {
  // Add particle at tail
  if(snake.length > 0) {
    particles.push({
      x: snake[snake.length-1].x,
      y: snake[snake.length-1].y,
      opacity: 0.8,
      size: gridSize
    });
  }
  
  // Update and filter
  particles = particles.filter(p => {
    p.opacity -= 0.02;
    p.size *= 0.95;
    return p.opacity > 0;
  });
  
  // Draw
  particles.forEach(p => {
    ctx.globalAlpha = p.opacity;
    ctx.fillStyle = '#00ff00';
    ctx.fillRect(p.x, p.y, p.size, p.size);
  });
  ctx.globalAlpha = 1;
}

// 3. Power-up food
function spawnFood() {
  const random = Math.random();
  return {
    x: Math.floor(Math.random() * canvas.width / gridSize) * gridSize,
    y: Math.floor(Math.random() * canvas.height / gridSize) * gridSize,
    type: random < 0.7 ? 'normal' : random < 0.9 ? 'golden' : 'slow',
    color: random < 0.7 ? '#ff0000' : random < 0.9 ? '#ffd700' : '#4169e1'
  };
}