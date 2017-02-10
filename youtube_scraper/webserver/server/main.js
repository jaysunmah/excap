import { Meteor } from 'meteor/meteor';

// var adminPassword = "henryssobadatthisgamelmao123"
var adminPassword = "123"

Meteor.startup(() => {
  Meteor.publish("projects", function () {
    return Meteor.Projects.find({});
  });
  Meteor.publish("myuser", function() {
    return Meteor.users.find({_id: this.userId});
  })
});

function decreaseTime(lobbyID) {
	var lobby = Meteor.Games.findOne({lobbyID: lobbyID});
	if (lobby) {
		var timeLeft = lobby.timeRemaining - 1;
		Meteor.Games.update({lobbyID: lobbyID}, {$set: {timeRemaining: timeLeft}});
		if (timeLeft == 0) {
			Meteor.clearInterval(lobby.intervalID);
		}
	}
}
function runRound(length, lobbyID) {
	var intervalID = Meteor.setInterval(function() {decreaseTime(lobbyID)}, 1000);
	Meteor.setTimeout(function() { Meteor.clearInterval(intervalID)}, 1000 * length + 1000);
}

Meteor.methods({
  'runScript': function(username, password) {
    this.unblock();
    return HTTP.get("http://127.0.0.1:5000/runscript/" + username + "/" + password);
  },
});
