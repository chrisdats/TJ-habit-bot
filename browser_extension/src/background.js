pubnub = new PubNub({
  publishKey : 'pub-c-9008e2a2-1e7e-40a6-aa4e-a9f6ddffb04d',
  subscribeKey : 'sub-c-c00d7a36-13bb-11e8-a8e8-9e7f09a8f511',
  ssl: true
})

function broadcast(message) {
  var publishConfig = {
    channel : "tab_activity",
    message : message
  }
  pubnub.publish(publishConfig, function(status, response) {
      console.log(status, response);
  })
}

function formatTime(t) {
  var time = new Date(t);
  return time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds();
}

var BAD_HOSTNAMES = ["www.facebook.com", "www.reddit.com"];

function onSessionStart(session) {
  console.log("START", formatTime(session.startTime), session.url);
  var url = new URL(session.url);
  var message = BAD_HOSTNAMES.includes(url.hostname) ? 'BAD' : 'GOOD'
  broadcast(message);
  if (true && message == 'BAD') {
    alert('Alert: You indicated that you would like to avoid this website!');
  }
}

function onSessionEnd(session) {
  console.log("END", formatTime(session.endTime), session.url);
}
var stopTracking = startTrackingActivity(onSessionStart, onSessionEnd);
