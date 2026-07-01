// dashboard.js - Simple Chart.js rendering script

document.addEventListener("DOMContentLoaded", function() {

  // 1. Recommended Careers spread (Bar Chart)
  var careerCanvas = document.getElementById("careerChart");
  if (careerCanvas && typeof careerData !== "undefined") {
    var labels = Object.keys(careerData);
    var values = Object.values(careerData);

    new Chart(careerCanvas, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Recommendations Count',
          data: values,
          backgroundColor: '#2D6A4F', // Green bar color
          borderColor: '#1B4332',
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            ticks: { stepSize: 1 }
          }
        }
      }
    });
  }

  // 2. Readiness Categories (Pie Chart)
  var readinessCanvas = document.getElementById("readinessChart");
  if (readinessCanvas && typeof readinessData !== "undefined") {
    var labels = Object.keys(readinessData);
    var values = Object.values(readinessData);

    new Chart(readinessCanvas, {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
          data: values,
          backgroundColor: ['#2D6A4F', '#F4A300', '#0DCAF0', '#DC3545'] // Green, Yellow, Blue, Red
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    });
  }

  // 3. User Skill Radar Chart
  var radarCanvas = document.getElementById("skillsRadar");
  if (radarCanvas && typeof skillsData !== "undefined" && Object.keys(skillsData).length > 0) {
    var labels = Object.keys(skillsData);
    var values = Object.values(skillsData);

    new Chart(radarCanvas, {
      type: 'radar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Your Level',
          data: values,
          backgroundColor: 'rgba(244, 163, 0, 0.2)', // Yellow tint
          borderColor: '#F4A300',
          pointBackgroundColor: '#1B4332'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          r: {
            angleLines: { display: true },
            suggestedMin: 0,
            suggestedMax: 10
          }
        }
      }
    });
  }

});
