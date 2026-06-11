# Ambiguity Checklist

When reviewing requirements, scan for these dangerous, ambiguous words. If found, flag them and ask the stakeholder to provide a quantifiable metric.

## 1. Subjective Adjectives
These words mean different things to different people.
- [ ] Fast / Quickly / Real-time *(Ask: "What is the acceptable latency in milliseconds?")*
- [ ] User-friendly / Intuitive *(Ask: "How do we measure this? Clicks to complete? Task success rate?")*
- [ ] Robust / Reliable *(Ask: "What is the expected uptime SLA? 99.9%?")*
- [ ] Large / Heavy *(Ask: "Large as in 5MB or 50GB?")*
- [ ] Secure *(Ask: "What specific security standards or encryption levels are required?")*

## 2. Unbounded Absolutes
These words are often technically impossible to guarantee 100% of the time.
- [ ] Always / Never *(Ask: "Is there any exception? What happens during a system outage?")*
- [ ] All / None *(Ask: "Does 'all users' include suspended accounts or admins?")*

## 3. Vague Verbs
These words describe an intent, but not a behavior.
- [ ] Handle / Manage *(Ask: "What exactly does 'manage' mean? Create, Read, Update, Delete?")*
- [ ] Support *(Ask: "Does 'support offline mode' mean read-only access or full read/write sync?")*
- [ ] Optimize *(Ask: "Optimize for what? Speed, memory, cost?")*

## 4. Ambiguous Pronouns
These create confusion about what object is being acted upon.
- [ ] "It" / "They" *(Ask: "Does 'it' refer to the user's cart or the specific item?")*

## 5. Loophole Words
These give developers permission to ignore the requirement.
- [ ] Generally / Usually / Often
- [ ] Etc. / And so on
- [ ] If possible / Where applicable
