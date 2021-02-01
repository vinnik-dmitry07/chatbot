import json
from datetime import datetime, timedelta


def partition(alist, indices):
    return [alist[a:b] for a, b in zip([0] + indices, indices + [None])]


with open('dorm16.json', 'r', encoding='utf8') as f:
    tg_messages = json.load(f)['messages']

messages = []
for msg in tg_messages:
    if (
            'from' in msg and
            'from_id' in msg and
            'mime_type' not in msg and
            msg['text'] and
            isinstance(msg['text'], str)
    ):
        msg['date'] = datetime.strptime(msg['date'], '%Y-%m-%dT%H:%M:%S')
        messages.append(msg)

episode_dt = timedelta(minutes=30)
joined_messages = [messages[0]]
for i in range(1, len(messages)):
    if (
            messages[i - 1]['from_id'] == messages[i]['from_id'] and
            messages[i - 1]['date'] - messages[i]['date'] <= episode_dt
    ):
        joined_messages[-1]['text'] += '\n' + messages[i]['text']
    else:
        joined_messages.append(messages[i])

time_diffs = [joined_messages[i + 1]['date'] - joined_messages[i]['date'] for i in range(len(joined_messages) - 1)]
split_positions = [i + 1 for i in range(len(time_diffs)) if time_diffs[i] > episode_dt]
episodes = partition(joined_messages, split_positions)

human_readable = False
with open('output.jsonl', 'w', **({'encoding': 'utf8'} if human_readable else {})) as outfile:
    for episode in episodes:
        dialog = [
            {
                'id': msg['from_id'],  # ''.join(e for e in msg['from'] if e.isalnum()).translate(tl_table),
                'text': msg['text'],
            } for msg in episode
        ]
        if len(dialog) >= 2:
            episode = {'dialog': [dialog]}
            json.dump(episode, outfile, **({'ensure_ascii': False} if human_readable else {}))
            outfile.write('\n')
