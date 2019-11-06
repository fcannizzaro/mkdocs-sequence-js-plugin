const init = () => {

	const diagrams = document.querySelectorAll("div[id*=diagram]");

	diagrams.forEach(diagram => {

		diagram.addEventListener('click', () =>
			diagram.classList.toggle('fullscreen-diagram')
		)

		window.addEventListener("keydown", (event) =>
			diagram.classList.remove('fullscreen-diagram'), true);

	});

}

document.addEventListener('DOMContentLoaded', init, false);