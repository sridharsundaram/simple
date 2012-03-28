    (function(){
      var webappCache = window.applicationCache;
      var progressDiv = document.getElementById('progressDiv');
      var lessonDiv = document.getElementById('lesson');
           
      switch (webappCache.status) {
      case 0:
        console.log("Cache status: Uncached");
        break;
      case 1:
        console.log("Cache status: Idle");
        break;
      case 2:
        console.log("Cache status: Checking");
        break;
      case 3:
        console.log("Cache status: Downloading");
        progressDiv.style.display = "";
        break;
      case 4:
        console.log("Cache status: Updateready");
        break;
      case 5:
        console.log("Cache status: Obsolete");
        break;
      default:
        console.log("Cache status: unknown");
      }
      
      function noupdateCache() {
        console.log("No update to cache found");
        progressDiv.style.display = "none";
        lessonDiv.style.display = "";
      }
      function doneCache() {
        console.log("Cache has finished downloading");
        progressDiv.style.display = "none";
        lessonDiv.style.display = "";
      }

      function progressCache(event) {
        console.log("Downloading cache..." + event.loaded + " " + event.total);
        progressDiv.style.display = "";
      }
      function updateCache() {
        webappCache.swapCache();
        console.log("Cache has been updated due to a change found in the manifest");
        if (confirm('The next scene has been downloaded. Play it?')) {
          window.location.reload();
        }
        progressDiv.style.display = "none";
        lessonDiv.style.display = "";
      }
      function errorCache() {
        console.log("You're either offline or something has gone horribly wrong.");
      }
      webappCache.addEventListener("progress", progressCache, false);
      webappCache.addEventListener("cached", doneCache, false);
      webappCache.addEventListener("noupdate", noupdateCache, false);
      webappCache.addEventListener("updateready", updateCache, false);
      webappCache.addEventListener("error", errorCache, false);
    })();
