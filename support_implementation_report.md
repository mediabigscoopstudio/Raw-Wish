# RAWWISH TODAY SUPPORT & ORDER MANAGEMENT IMPLEMENTATION PLAN

## CURRENT ARCHITECTURE
- **Authentication**: Google One Tap/OAuth is fully implemented. Users are mapped to a `Customers` profile.
- **Orders**: `Order` and `OrderItem` models exist but lack a human-readable, sequence-based ID (`display_order_id`).
- **Support**: A generic `Support` model exists (Name, Email, Message) likely used for contact forms, but it lacks relational integrity to Customers, Orders, or Products, and lacks chat/multi-turn capabilities.
- **Customer UI**: A generic account dropdown exists but points to placeholder `#` links.
- **Admin UI**: An orders Kanban board exists. Support is just a flat list of contact-us forms.

## REUSE
- **Existing Models**: `User`, `Customers`, `Order`, `OrderItem`, `Product`, `Variant`.
- **Existing Admin Template**: `dash/base.html` and UI components.
- **Existing Authentication**: We will strictly filter orders and support queries using `request.user.customer_account`.

## CHANGES
- `Order` model will receive a `display_order_id` (e.g. #KT26092500421).
- `dash/models.py` will be expanded with new models (see below).
- `main/views.py` will get new customer-facing views for Orders and Support.
- `dash/views.py` will have the `support` view rewritten to a Kanban system.
- `template/main/base.html` dropdown will be updated.

## NEW COMPONENTS
- `SequenceCounter` model (for transaction-safe ID generation).
- `SupportQuery` model (links Customer, Order, OrderItem).
- `SupportMessage` model (handles Chatbot, Customer, and Human Agent replies).
- Customer Order List & Detail templates (`my_orders.html`, `my_order_detail.html`).
- Customer Support UI (`support_list.html`, `support_chat.html`).
- Admin Kanban Support UI (`dash/support/kanban.html`).
- Chatbot logic in Python (stateless, intent-based matching linked to Django DB).

## DATABASE MIGRATIONS
- Create `SequenceCounter`.
- Add `display_order_id` to `Order` (allow null first, populate via data migration/script, then enforce unique).
- Create `SupportQuery` and `SupportMessage`.
