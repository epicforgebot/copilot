sap.ui.define([
  'sap/ui/core/mvc/Controller'
], function(Controller) {
  'use strict';
  return Controller.extend('copilot.controller.ResponseDisplay', {
    onInit: function() {
      var oEventBus = sap.ui.getCore().getEventBus();
      oEventBus.subscribe('messageChannel', 'newMessage', this.onNewMessage, this);
    },
    onNewMessage: function(sChannel, sEvent, oData) {
      var oText = this.byId('responseText');
      oText.setText(oData.sender + ': ' + oData.message);
    }
  });
});