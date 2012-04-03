// Copyright 2012 Maza Learn Pvt Ltd. All Rights Reserved.
// @author Sridhar Sundaram
/**
 * @fileoverview Implements the Maza interface in javascript.
 * This will work with either an Android client or with normal browsers.
 * @author sridhar.sundaram@gmail.com (Sridhar Sundaram)
 */


var NUM_ANSWER_CHOICES = 4;

Maza = function() {
};

// android interface is defined internally for Android webview.
// We will first define a browse version for Maza API and 
//  override with Android specific version if available.

  Maza.prototype.isBrowser = true;

  Maza.prototype.browser = 'chrome';
  // Let us find out which browser this is.
  if (navigator.userAgent.indexOf('nokia') != -1) {
    Maza.prototype.browser = 'nokiaS40';
  }
  
  Maza.prototype.getMobileNumber = function() {
    return "";
  }
  
  /**
   * Plays the audio corresponding to url.
   * @param url - url of the audio
   */
  Maza.prototype.playAudio = function(url) {
    if (Maza.prototype.browser == 'nokiaS40') {
      mwl.loadURL(url); // rtsp url
      return;
    }
    var e = document.getElementById("audio");
    if (!e) {
        e = document.createElement("audio");
        e.id = "audio";
        document.body.appendChild(e);
    }
    e.pause();
    e.src = url;
    e.load();
    e.play();
  }
} 

if (typeof android != "undefined") { // Android Webview
  Maza.prototype.isBrowser = false;
  Maza.prototype.getMobileNumber = function() { return android.getMobileNumber(); }
  if (android.getVersion() <= 9) { // After version 9, this got fixed.
    Maza.prototype.playAudio = function(url) { android.playAudio(url); }
  }
}

Maza.prototype.playAudioSequence = function(urlArray) {
  if (urlArray.length == 0) return;
  var e = document.getElementById("audio");
  if (!e) {
      e = document.createElement("audio");
      e.id = "audio";
      e.style.display = "none";
      document.body.appendChild(e);
  }
  
  var url = urlArray.shift();
  e.src = url;
  e.load();
  e.addEventListener('ended', function() { Maza.prototype.playAudioSequence(urlArray); });
  e.play();
}

function makeAbsoluteUrl(relativeUrl) {
  return location.protocol + '//' + location.host + "/" + relativeUrl;
}

maza = new Maza();

// Check if a new app-cache is available on page load.
window.addEventListener('load', function(e) {
  window.applicationCache.addEventListener('updateready', function(e) {
    if (window.applicationCache.status == window.applicationCache.UPDATEREADY) {
      // Browser downloaded a new app cache.
      // Swap it in and reload the page to get the new hotness.
      window.applicationCache.swapCache();
      if (confirm('The next scene has been downloaded. Play it?')) {
        window.location.reload();
      }
    } else {
      // Manifest didn't change - Nothing new to serve
    }
  }, false);
}, false);
