// var renderDelay = 200;

Template.projects.events({
  'click #goHome' (event) {
    Session.set('renderedLanding', true);
    var cb = function() {
      Router.go('/');
    }
    $('#projectsContainer').transition({
      animation: 'fade left',
      duration: transitionDelay,
      onHide: cb
    });
  },
});

function filterIndices(index) {
  var projects = Meteor.Projects.find({}).fetch();
  var result = [];
  projects.forEach(function(val, i) {
    if (i % 3 == index) {
      result.push(val);
    }
  });
  return result;
}

Template.projects.helpers({
  projects: function(i) {
    return filterIndices(i);
  },
  isCollapsed: function() {
    return Session.get('collapsedProjects');
  },
  allProjects: function() {
    return Meteor.Projects.find({}).fetch();
  },
});

function showContainers() {
  // $('.project.container').addClass('transition hidden');
  function animateContainers(i) {
      $('.project.container.' + i).transition({
        animation : 'scale',
        reverse   : 'auto', // default setting
        interval  : renderDelay,
        onShow  : cb
      });
  }
  if (!(Session.get('renderedProjects'))) {

    var count = 0;
    var cb = function() {
      count ++;
      if (count == Meteor.Projects.find({}).fetch().length) {
        Session.set('renderedProjects', true);
      }
    }

    animateContainers('0');
    animateContainers('1');
    animateContainers('2');
  }
}

function checkCollapsedProjects() {
  // if ($('#projectItem0').width() > ($(window).width() / 2)) {
  if ($(window).width() <= 767) { //bleh, figure out a better way for this >.<
    Session.set('collapsedProjects', true);
  } else {
    Session.set('collapsedProjects', false);
  }
}

Template.projects.onRendered(function() {
  Session.set('renderedProjects', false)
  window.onresize = function(event) {
    checkCollapsedProjects();
  };

  checkCollapsedProjects();
  $('.ui.menu')
  .on('click', '.item', function() {
    if(!$(this).hasClass('dropdown')) {
      $(this)
        .addClass('active')
        .siblings('.item')
        .removeClass('active');
    }
  });
  $('#projectsContainer').transition({
    animation: 'fade left',
    duration: transitionDelay,
    onShow: showContainers
  });
  // if (!(Session.get('renderedProjects'))) {
    // Meteor.setTimeout(showContainers, renderDelay);
  // }
});
