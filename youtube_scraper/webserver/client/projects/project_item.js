Template.project_item.events({
  'click #joinGame' (event) {
    Session.set('joiningGame', true);
  },
});

Template.project_item.helpers({
  itemIndex: function() {
    return getIndexOf(this) % 3;
  },
  totalIndex: function() {
    return getIndexOf(this);
  },
  isHidden: function() {
    if(!(Session.get('renderedProjects')) && getIndexOf(this) != -1) {
      return 'hidden';
    } else {
      return 'visible';
    }
  }
});

function getIndexOf(obj) {
  var projects = Meteor.Projects.find({}).fetch();
  for (var i = 0; i < projects.length; i++) {
    if (projects[i]._id._str == obj._id._str) {
      return i;
    }
  }
  return -1;
}

Template.project_item.onRendered(function() {
  // console.log(getIndexOf(this.data));
});
