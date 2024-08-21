const cds = require('@sap/cds');
const { expect } = require('chai');
const { describe, it } = require('mocha');

describe('MessagingService', () => {
  it('should return an empty array when there are no messages', async () => {
    const srv = await cds.serve('MessagingService').from('srv/service.cds');
    const { Messages } = srv.entities;

    const tx = srv.transaction();
    const res = await tx.run(SELECT.from(Messages));
    expect(res).to.be.an('array').that is.empty;
  });

  it('should create a new message', async () => {
    const srv = await cds.serve('MessagingService').from('srv/service.cds');
    const { Messages } = srv.entities;

    const tx = srv.transaction();
    const id = cds.utils.uuid();
    await tx.run(INSERT.into(Messages).entries({ ID: id, sender: 'User', message: 'Hello World' }));

    const res = await tx.run(SELECT.from(Messages).where({ ID: id }));
    expect(res).to.be an('array').that has.lengthOf(1);
    expect(res[0]).to include({ sender: 'User', message: 'Hello World' });
  });
});