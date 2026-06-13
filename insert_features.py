with open('README.md', 'r', encoding='utf-16') as f:
    content = f.read()

features = """

## Features

### Landing Page

Sakina's homepage introduces the platform to anonymous visitors with a clear value proposition and calls to action.

![Landing page](docs/features/landing-page.png)

### User Registration

New users can register with a username, email, and password.

![Sign up page](docs/features/sign-up-page.png)

### Authentication

Users sign in securely. A flash message confirms successful login and the navbar updates to show authenticated links.

![Sign in success](docs/features/feature-sign-in-success.png)

### Stripe Subscription

After registration, users are directed to a Stripe checkout page to subscribe for \u20ac9.99 per month before accessing any features.

![Stripe checkout](docs/features/feature-stripe-checkout.png)

### Create Profile

Subscribed users complete a detailed profile covering faith, background, family goals, and personal information. Age validation ensures users are 18 or over.

![Create profile](docs/features/feature-create-profile.png)

![Age validation](docs/features/age-validation.png)

### Profile Detail

Users can view their own profile with all sections displayed clearly, and access edit, matches, and account deletion options.

![Profile detail](docs/features/feature-profile-detail-1.png)

![Profile detail lower](docs/features/feature-profile-detail-2.png)

### Compatibility Matches

The matching algorithm calculates compatibility scores against all other profiles. Before running, the matches page shows an empty state. After refreshing, ranked matches appear with photos, key details, and scores.

![Matches empty](docs/features/feature-matches-empty.png)

![Matches](docs/features/feature-matches.png)

### Profile View

Subscribers can view another user's full profile, including their compatibility score.

![Profile match view](docs/features/feature-profile-match.png)

### Messaging

Users can send a message directly from a match's profile page.

![Send message](docs/features/feature-send-message.png)

### Conversation

The conversation view shows the full message thread between two users.

![Conversation](docs/features/feature-conversation-1.png)

![Conversation reply](docs/features/feature-conversation-reply-youssef.png)

### Inbox

The inbox displays all received messages. An unread count appears in the navbar when new messages arrive.

![Inbox notification](docs/features/feature-inbox-notification-youssef.png)

![Inbox](docs/features/feature-inbox-youssef.png)

"""

content = content.replace('### Implementation', features + '### Implementation', 1)
content = content.replace('- [ChatGPT](https://chatgpt.com/) \u2014 debugging assistance\n', '')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')