import { Meteor } from 'meteor/meteor';

Meteor.startup(() => {

});

Meteor.methods({
  'youtubeLogin': function(username, password) {
    // this.unblock();
    return HTTP.get("http://127.0.0.1:8080/runscript/youtube/" + username + "/" + password);
  },
  'saveImages': function(username, password) {
    // this.unblock();
    return HTTP.get("http://127.0.0.1:8080/runscript/save_images/" + username + "/" + password);
  },
  'parseImages': function(username, password) {
    // this.unblock();
    return HTTP.get("http://127.0.0.1:8080/runscript/parse_images/" + username + "/" + password);
  },
  'arrangeFiles': function(username, password) {
    // this.unblock();
    return HTTP.get("http://127.0.0.1:8080/runscript/arrange_files/" + username + "/" + password);
  },
});
