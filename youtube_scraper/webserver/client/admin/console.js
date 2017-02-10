Template.console.events({
  'change #imagePreview' (event) {
    var preview = Session.get('preview') || {};
    preview.image = $('#imagePreview').val();
    Session.set('preview', preview);
    Session.set('imagePreview', $('#imagePreview').val());
  },
  'change #titlePreview, keyup #titlePreview' (event) {
    var preview = Session.get('preview') || {};
    preview.title = $('#titlePreview').val();
    Session.set('preview', preview);
  },
  'change #descriptionPreview, keyup #descriptionPreview' (event) {
    var preview = Session.get('preview') || {};
    preview.description = $('#descriptionPreview').val();
    Session.set('preview', preview);
  },
  'change #datePreview, keyup #datePreview' (event) {
    var preview = Session.get('preview') || {};
    preview.date = $('#datePreview').val();
    Session.set('preview', preview);
  },
  'click #languagePreview, change #languagePreview' (event) {
    var languages = $('.ui.multiple.selection.dropdown').dropdown('get values')
    var preview = Session.get('preview') || {};
    preview.languages = languages;
    Session.set('preview', preview);
  },
  'click #addProject' (event) {
    // Meteor.Projects.insert(Session.get('preview'));
    Meteor.call('insertProject', Session.get('preview'));
  }
});


Template.console.helpers({
  templateData: function() {
    return {
      _id: {
        _str: ""
      },
      image: Session.get('preview').image,
      title: Session.get('preview').title,
      description: Session.get('preview').description,
      date: Session.get('preview').date,
      languages: (Session.get('preview').languages || []).join(", "),
    };
  }
});

Template.console.onRendered(function() {
  Session.set('preview', {
    image: "",
    title: "",
    description: "",
    date: "",
    languages: []
  });
  // $('.ui.multiple.selection.dropdown').dropdown();
  Meteor.setTimeout(function() {
    $('.ui.multiple.selection.dropdown').dropdown();
  }, 100);
});
