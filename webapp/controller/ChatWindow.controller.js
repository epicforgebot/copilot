sap.ui.define([
  'sap/ui/core/mvc/Controller',
  'sap/ui/model//JSONModel'
], function(Controller, JSONModel) {
  'use strict';
  return Controller.extend('copilot.controller.ChatWindow', {
    onInit: function() {
      var oModel = new JSONModel({
        messages: []
      });
      this.getView().setModel(oModel);
    },
    addMessage: function(sSender, sMessage) {
      var oModel = this.getView().getModel();
      var aMessages = oModel.getProperty('/messages');
      aMessages.push({
        sender: sSender,
        message: sMessage
      });
      oModel.setProperty('/messages', aMessages);
    }
  });
});