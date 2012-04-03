// Copyright 2012 Maza Learn Pvt Ltd. All Rights Reserved.

/**
 * @fileoverview Implements the Maza AppCache sync in javascript.
 * @author sridhar.sundaram@gmail.com (Sridhar Sundaram)
 */

(function(){
  var webappCache = window.applicationCache;
  var progressDiv = document.getElementById('progressDiv');
  var progressBar = document.getElementById('progressBar');
  var lessonDiv = document.getElementById('lesson');
  var numCacheFiles = 0;
  var numDownloadedFiles = 0;
  
  function showProgressHideMain(show) {
    if (show) {
      progressDiv.style.display = "";
      lessonDiv.style.display = "none";
    } else {
      lessonDiv.style.display = "";
      progressDiv.style.display = "none";      
    }   
  }
  switch (webappCache.status) {
  case webappCache.UNCACHED:
    console.log("Cache status: Uncached");
    break;
  case webappCache.IDLE:
    console.log("Cache status: Idle");
    showProgressHideMain(false);
    break;
  case webappCache.CHECKING:
    console.log("Cache status: Checking");
    break;
  case 3:
    console.log("Cache status: Downloading");
    showProgressHideMain(true);
    break;
  case webappCache.UPDATEREADY:
    console.log("Cache status: Updateready");
    break;
  case webappCache.OBSOLETE:
    console.log("Cache status: Obsolete");
    break;
  default:
    console.log("Cache status: unknown");
  }
  
  function noupdateCache() {
    console.log("No update to cache found");
    showProgressHideMain(false);
  }
  function doneCache() {
    console.log("Cache has finished downloading");
    showProgressHideMain(false);
  }

  function progressCache(event) {
    if (numCacheFiles == 0) {
      numCacheFiles = findNumCacheFiles();
    }
    numDownloadedFiles++;
    console.log("Downloading " + numDownloadedFiles + " of " + numCacheFiles);
    progressBar.style.backgroundPositionX =
        100 * (1 - (numDownloadedFiles / numCacheFiles)) + '%';
    if (numDownloadedFiles == numCacheFiles) {
      showProgressHideMain(false);      
    }
  }

  function updateCache() {
    showProgressHideMain(false);
    if (webappCache.status != webappCache.UPDATEREADY) {
      return;
    }
    webappCache.swapCache();
    console.log("Cache has been updated due to a change found in the manifest");
    if (confirm('Lesson downloaded. Play?')) {
      window.location.reload();
    }
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
