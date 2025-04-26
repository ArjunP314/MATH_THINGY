document.addEventListener("DOMContentLoaded", () => {
  // Example static data (replace with fetch to your backend later)
  const proofs = [
    {
      title: "Proof of Pythagoras Theorem",
      description: "A visual and algebraic derivation of a² + b² = c²",
      steps: ["Draw a right triangle...", "Use square areas..."]
    },
    {
      title: "Euler’s Formula",
      description: "Demonstrates e^(iπ) + 1 = 0",
      steps: ["Start from Taylor series...", "Substitute imaginary x..."]
    }
  ];

  const container = document.getElementById("proofs-container");
  proofs.forEach(proof => {
    const card = document.createElement("div");
    card.className = "proof-card";
    card.innerHTML = `
      <h3>${proof.title}</h3>
      <p>${proof.description}</p>
      <ul>${proof.steps.map(step => `<li>${step}</li>`).join('')}</ul>
    `;
    container.appendChild(card);
  });
});
