sap.ui.define([
  'sap/ui/test/opaQunit',
  'sap/ui/test/Opa5',
  'copilot/controller/ChatWindow'
], function(opaTest, Opa5) {
  'use strict';
  Opa5.extendConfig({
    arrangements: new Opa5({
      iStartMyApp: function() {
        this.iStartMyUIComponent({
          componentConfig: {
            name: 'copilot'
          }
        });
      }
    }),
    viewNamespace: 'copilot.view.'
  });

  opaTest('Should add a message to the chat window', function(Given, When, Then) {
    Given.iStartMyApp();
    When.onTheChatWindowPage.iAddMessage('User', 'Hello World');
    Then.onTheChatWindowPage.iShouldSeeTheMessage('User', 'Hello World');
  });
});