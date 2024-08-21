sap.ui.define([
  'sap/ui/core/UIComponent',
  'sap/ui/model//JSONModel'
], function(UIComponent, JSONModel) {
  'use strict';
  return UIComponent.extend('copilot.Component', {
    metadata: {
      manifest: ''
    },
    init: function() {
      UIComponent.prototype.init.apply(this, arguments);
    }
  });
});