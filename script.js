document.addEventListener("DOMContentLoaded", function () {
    const apiKey = "AIzaSyDFwhl52JdgQsR1L13qhlXqsneVWVbVFdU";
    const channelId = "UCPUh5o9YJ732EAR8z82ljvg"; // Sostituisci con il tuo channel ID
    const videoContainer = document.getElementById("video-container");
    
    async function fetchVideos() {
        try {
            const response = await fetch(`https://www.googleapis.com/youtube/v3/search?key=${apiKey}&channelId=${channelId}&part=snippet,id&order=date&maxResults=12`);
            const data = await response.json();
            
            if (data.items) {
                videoContainer.innerHTML = "";
                data.items.forEach((item) => {
                    if (item.id.videoId) {
                        const videoElement = document.createElement("div");
                        videoElement.classList.add("video-item");
                        videoElement.innerHTML = `
                            <iframe src="https://www.youtube.com/embed/${item.id.videoId}" frameborder="0" allowfullscreen></iframe>
                            <p>${item.snippet.title}</p>
                        `;
                        videoContainer.appendChild(videoElement);
                    }
                });
            } else {
                videoContainer.innerHTML = "<p>Nessun video trovato.</p>";
            }
        } catch (error) {
            console.error("Errore nel caricamento dei video:", error);
            videoContainer.innerHTML = "<p>Errore nel recupero dei video. Riprova più tardi.</p>";
        }
    }
    
    fetchVideos();
});
