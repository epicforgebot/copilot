using { copilot.Messages } from '../db/schema';

service MessagingService {
  entity Messages as projection on copilot.Messages;
}