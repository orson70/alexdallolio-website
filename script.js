document.addEventListener("DOMContentLoaded", async function () {
  const apiKey = "INSERISCI-LA-TUA-API-KEY"; // Sostituisci con la tua API key YouTube
  const channelId = "UCPUh5o9YJ732EAR8z82ljvg"; // Sostituisci con il tuo channelId
  const maxResults = 12;
  const videoContainer = document.getElementById("video-container");

  async function fetchVideos() {
    try {
      const response = await fetch(
        `https://www.googleapis.com/youtube/v3/search?key=${apiKey}&channelId=${channelId}&part=snippet,id&order=date&maxResults=${maxResults}`
      );
      const data = await response.json();
      if (data.items) {
        displayVideos(data.items);
      } else {
        throw new Error("Nessun video trovato");
      }
    } catch (error) {
      console.error("Errore nel caricamento dei video", error);
      videoContainer.innerHTML = "<p>Impossibile caricare i video.</p>";
    }
  }

  function displayVideos(videos) {
    videoContainer.innerHTML = "";
    if (!videos || videos.length === 0) {
      videoContainer.innerHTML = "<p>Nessun video trovato.</p>";
      return;
    }
    videos.forEach(video => {
      if (video.id.videoId) {
        const videoId = video.id.videoId;
        const title = video.snippet.title;
        const videoItem = document.createElement("div");
        videoItem.classList.add("video-item");
        videoItem.innerHTML = `
          <iframe src="https://www.youtube.com/embed/${videoId}"
                  frameborder="0"
                  allowfullscreen></iframe>
          <p>${title}</p>
        `;
        videoContainer.appendChild(videoItem);
      }
    });
  }

  fetchVideos();
});