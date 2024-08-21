sap.ui.define([
  'sap/ui/core/mvc/Controller'
], function(Controller) {
  'use strict';
  return Controller.extend('copilot.controller.MessageInput', {
    onSendMessage: function() {
      var oInput = this.byId('messageInput');
      var sMessage = oInput.getValue();
      if (sMessage.trim()) {
        var oEventBus = sap.ui.getCore().getEventBus();
        oEventBus.publish('messageChannel', 'newMessage', { sender: 'User', message: sMessage });
        oInput.setValue('');
      }
    }
  });
});