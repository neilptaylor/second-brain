function buildSnapshotForm() {
  var f = FormApp.create('Your Snapshot');
  f.setTitle('Your Snapshot');
  f.setDescription(
    "Very soon, we'll sit down for an hour and a half and talk about your life as it is right now. The year you've actually had: the bits you'd tell a mate over a pint, and the bits you haven't told anyone yet.\n\n" +
    "This form is how I get ready, so you arrive with more than \"erm, work's been busy\". There are no right answers, and a half-finished sentence is as useful to me as a polished one. Give it about 30 minutes, ideally with a cuppa and your photo roll open.\n\n" +
    "Everything you write here, and everything we record, is private to you. It's yours, to keep, share or never play to anyone. That's your call.\n\nNeil");
  f.setCollectEmail(true);
  f.setProgressBar(true);
  f.setConfirmationMessage("Thank you. That's me ready. See you very soon.\n\nNeil");

  f.addTextItem().setTitle('Your name').setRequired(true);

  f.addPageBreakItem().setTitle('Who it\'s for');
  f.addCheckboxItem().setTitle('When someone presses play on your Snapshot in years to come, who do you picture listening?')
    .setChoiceValues(['Me, looking back','My children','My partner','My grandchildren, one day']).showOtherOption(true).setRequired(true);
  f.addParagraphTextItem().setTitle('What might you want them to hear?')
    .setHelpText("A story, a feeling, something you've never quite said out loud.");

  f.addPageBreakItem().setTitle('Your people');
  f.addParagraphTextItem().setTitle("Who's in your household and close family?")
    .setHelpText("Names, how they're related to you, and dates of birth if you're happy to share.").setRequired(true);
  f.addParagraphTextItem().setTitle("Who else has been in your corner this year?")
    .setHelpText("A friend, a colleague, a neighbour. Just names and a few words on each.");

  f.addPageBreakItem().setTitle('How you see your life');
  f.addCheckboxItem().setTitle('Which of these have taken up the most room in your head this year?')
    .setHelpText('Tick up to four.')
    .setChoiceValues(['Family and kids','Partner','Friends','Work','Health, body','Health, mind','Faith or meaning','Home, a move, a place',"Something you're learning or making"])
    .showOtherOption(true)
    .setValidation(FormApp.createCheckboxValidation().requireSelectAtMost(4).build()).setRequired(true);
  f.addTextItem().setTitle('If you think about your life in a different way, chapters, seasons, a list on the fridge, tell me how.');

  f.addPageBreakItem().setTitle('This year, in moments');
  f.addParagraphTextItem().setTitle('Scroll back through your photos from the last twelve months. Which one says "this was my year"? Tell me what\'s in it.')
    .setHelpText('Email me the photo too if you like.').setRequired(true);
  f.addParagraphTextItem().setTitle('The high point. When did you think, "this is good"?').setRequired(true);
  f.addParagraphTextItem().setTitle('The hard bit. What did you get through?')
    .setHelpText('Share as much or as little as you want. Stories, not skeletons.').setRequired(true);
  f.addParagraphTextItem().setTitle('What surprised you, about life or about yourself?').setRequired(true);
  f.addTextItem().setTitle('Finish the sentence: "This was the year I..."').setRequired(true);

  f.addPageBreakItem().setTitle('Right now, and next');
  f.addTextItem().setTitle("What's a phrase you've said a lot this year?")
    .setHelpText('The thing your family would do an impression of.').setRequired(true);
  f.addTextItem().setTitle('What song captures your year? Or which artist have you been playing on repeat?')
    .setHelpText('The one that goes in the background of your Snapshot. Song name and artist if you can.');
  f.addParagraphTextItem().setTitle('Looking twelve months ahead, what are you hoping for?').setRequired(true);
  f.addParagraphTextItem().setTitle('When you listen back in ten years, what do you hope you\'ll hear?').setRequired(true);
  f.addTextItem().setTitle('Anything off limits?');
  f.addMultipleChoiceItem().setTitle("One last thing, and it's entirely up to you.")
    .setHelpText("I'm starting to write a book about families and the conversations we don't get round to having. If something you say could help someone else, would you be happy for me to use it, fully anonymously? No names, no places, nothing that could point back to you.")
    .setChoiceValues(['Yes, happy for you to use it anonymously','Ask me first','No thanks']);

  DriveApp.getFileById(f.getId()).moveTo(DriveApp.getFolderById('1J73T6orFlYyqwNfBjUgRu5P8ZLdUHKon'));
  Logger.log('Edit: ' + f.getEditUrl());
  Logger.log('Share: ' + f.getPublishedUrl());
}
