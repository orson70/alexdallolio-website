document.addEventListener("DOMContentLoaded", async function () {
    const videoContainer = document.getElementById("video-container");
    if (!videoContainer) {
        // Se non c'è il container per i video, non eseguire nulla.
        return;
    }
    
    // Nota bene: l'API key è esposta qui. In un ambiente di produzione, valuta l'uso di un backend per proteggerla.
    const apiKey = "AIzaSyDFwhl52JdgQsR1L13qhlXqsneVWVbVFdU";
    const channelId = "UCPUh5o9YJ732EAR8z82ljvg";
    const maxResults = 12;

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
                const videoElement = document.createElement("div");
                videoElement.classList.add("video-item");
                videoElement.innerHTML = `
                    <iframe width="100%" height="315" src="https://www.youtube.com/embed/${videoId}?rel=0" frameborder="0" allowfullscreen></iframe>
                    <p class="video-title">${title}</p>
                `;
                videoContainer.appendChild(videoElement);
            }
        });
    }

    fetchVideos();
});