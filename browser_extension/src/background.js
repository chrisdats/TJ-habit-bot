/* File: background.js
 * -------------------
 * This script defines an event page, which allows you
 * to have a "single long-running script to handle some
 * task or state."
 *
 * The general principle is that this script will register
 * to listen for Chrome events, and then be instantiated
 * when Chrome notices that event.
 *
 * 
 * Note: Since the event page is created and destroyed many
 * times throughout a browser session, you cannot store
 * instance state in global variables.
 */


// Initialize Firebase
var config = {
  apiKey: "AIzaSyBhPK2tRDJvXbMqNWWy-qvYx0WPnqMfFsM",
  authDomain: "monitor-a80a5.firebaseapp.com",
  databaseURL: "https://monitor-a80a5.firebaseio.com",
  projectId: "monitor-a80a5",
  storageBucket: "",
  messagingSenderId: "134254052426"
};

firebase.initializeApp(config);
db = firebase.database().ref('activity');

function logSessionEvent(session) {
  var newEntry = db.push();
  newEntry.set({
    url: session.url,
    startTime: session.startTime,
    endTime: session.endTime
  });
}

function formatTime(t) {
  var time = new Date(t);
  return time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds();
}

function onSessionStart(session) {
  console.log("OPEN", formatTime(session.startTime), session.url);
}

function onSessionEnd(session) {
  console.log("CLOSE", formatTime(session.endTime), session.url);
  logSessionEvent(session);
}

var stopTracking = startTrackingActivity(onSessionStart, onSessionEnd);
