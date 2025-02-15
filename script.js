document.addEventListener("DOMContentLoaded", function () {
    const API_KEY = "AIzaSyDFwhl52JdgQsR1L13qhlXqsneVWVbVFdU";
    const CHANNEL_ID = "UCPUh5o9YJ732EAR8z82ljvg";
    const videoGallery = document.getElementById("video-gallery");

    async function fetchVideos() {
        try {
            const response = await fetch(
                `https://www.googleapis.com/youtube/v3/search?key=${API_KEY}&channelId=${CHANNEL_ID}&part=snippet,id&order=date&maxResults=12`
            );
            const data = await response.json();
            displayVideos(data.items);
        } catch (error) {
            console.error("Errore nel recupero dei video:", error);
            videoGallery.innerHTML = "<p>Errore nel caricamento dei video.</p>";
        }
    }

    function displayVideos(videos) {
        videoGallery.innerHTML = "";
        videos.forEach((video) => {
            if (video.id.videoId) {
                const videoElement = document.createElement("div");
                videoElement.classList.add("video-item");
                videoElement.innerHTML = `
                    <iframe src="https://www.youtube.com/embed/${video.id.videoId}" frameborder="0" allowfullscreen></iframe>
                    <p>${video.snippet.title}</p>
                `;
                videoGallery.appendChild(videoElement);
            }
        });
    }

    fetchVideos();
});
