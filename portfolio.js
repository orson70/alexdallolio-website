document.addEventListener("DOMContentLoaded", async function () {
    const apiKey = "AIzaSyDFwhl52JdgQsR1L13qhlXqsneVWVbVFdU";
    const channelId = "UCPUh5o9YJ732EAR8z82ljvg";
    const maxResults = 12;
    const videoContainer = document.getElementById("video-container");

    async function fetchVideos() {
        try {
            const response = await fetch(
                `https://www.googleapis.com/youtube/v3/search?key=${apiKey}&channelId=${channelId}&part=snippet,id&order=date&maxResults=${maxResults}`
            );
            const data = await response.json();
            displayVideos(data.items);
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
                    <iframe width="100%" height="315" src="https://www.youtube.com/embed/${videoId}" frameborder="0" allowfullscreen></iframe>
                    <p>${title}</p>
                `;

                videoContainer.appendChild(videoElement);
            }
        });
    }

    fetchVideos();
});
