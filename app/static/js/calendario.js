let currentDate = new Date();
    const daysContainer = document.getElementById("days");
    const monthYearHeader = document.getElementById("month-year");
    const prevButton = document.getElementById("prev");
    const nextButton = document.getElementById("next");

    // Treinos passados pelo Django
    const treinos = JSON.parse('{{ treinos | escapejs }}');

    // Função para renderizar o calendário
    function renderCalendar() {
      const year = currentDate.getFullYear();
      const month = currentDate.getMonth();

      const firstDayOfMonth = new Date(year, month, 1).getDay();
      const lastDateOfMonth = new Date(year, month + 1, 0).getDate();

      monthYearHeader.textContent = `${currentDate.toLocaleDateString("pt-BR", {
        month: "long",
        year: "numeric",
      })}`;

      daysContainer.innerHTML = "";

      // Adiciona dias vazios antes do primeiro dia do mês
      for (let i = 0; i < (firstDayOfMonth === 0 ? 6 : firstDayOfMonth - 1); i++) {
        daysContainer.innerHTML += `<div class="day empty"></div>`;
      }

      // Preenche os dias do mês
      for (let day = 1; day <= lastDateOfMonth; day++) {
        const today = new Date().toDateString() === new Date(year, month, day).toDateString();
        const dayElement = document.createElement("div");
        dayElement.classList.add("day");
        if (today) dayElement.classList.add("today");

        dayElement.innerHTML = `<span>${day}</span>`;

        // Verifica se há algum treino para esse dia
        const treinoDoDia = treinos.filter(t => new Date(t.data_inicio).getDate() === day && new Date(t.data_inicio).getMonth() === month);

        treinoDoDia.forEach(treino => {
          const treinoElement = document.createElement("div");
          treinoElement.classList.add("event");
          treinoElement.innerHTML = `${treino.hora_inicio} - ${treino.hora_fim} - ${treino.tipo_treino}`;
          dayElement.appendChild(treinoElement);
        });

        daysContainer.appendChild(dayElement);
      }
    }

    // Navegação pelos meses
    prevButton.addEventListener("click", () => {
      currentDate.setMonth(currentDate.getMonth() - 1);
      renderCalendar();
    });

    nextButton.addEventListener("click", () => {
      currentDate.setMonth(currentDate.getMonth() + 1);
      renderCalendar();
    });

    // Renderiza o calendário ao carregar a página
    renderCalendar();