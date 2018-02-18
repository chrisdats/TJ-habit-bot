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
  var newEntry = activityRef.push();
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


  // console.log("START", formatTime(session.startTime), session.url);

  // var newEntry = db.push();
  // newEntry.set({
  //   url: 
  // });

  // db.set(url.hostname);
  // db.once('value').then(snapshot => console.log(snapshot.val()));

  // var message = BAD_HOSTNAMES.includes(url.hostname) ? 'BAD' : 'GOOD'
  // broadcast(message);
  // if (true && message == 'BAD') {
  //   alert('Alert: You indicated that you would like to avoid this website!');
  // }

// pubnub = new PubNub({
//   publishKey : 'pub-c-9008e2a2-1e7e-40a6-aa4e-a9f6ddffb04d',
//   subscribeKey : 'sub-c-c00d7a36-13bb-11e8-a8e8-9e7f09a8f511',
//   ssl: true
// });

// function broadcast(message) {
//   var publishConfig = {
//     channel : "tab_activity",
//     message : message
//   };
//   pubnub.publish(publishConfig, function(status, response) {
//       console.log(status, response);
//   });
// }
