import { Meteor } from 'meteor/meteor';

Meteor.startup(() => {

});

Meteor.methods({
  'runScript': function(username, password) {
    this.unblock();
    return HTTP.get("http://127.0.0.1:5000/runscript/" + username + "/" + password);
  },
});
