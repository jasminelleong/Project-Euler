import os
from datetime import datetime
from subprocess import call

expected_files = [f'{i:03d}.py' for i in range(1000)]
solutions_files = [file for file in expected_files if os.path.isfile(file)]


def write_progress_table(progress_info):
    readme = open('README.md', 'r')
    readme_lines = readme.read()
    readme_progress_index = readme_lines.find('## Progress')
    truncated_readme = readme_lines[:readme_progress_index] + '## Progress\n'
    num_suboptimal = 0
    for line in progress_info:
        if line['time'] > 30:
            num_suboptimal += 1

    progress_line = '### {} / {} Complete!\n\n'.format(len(progress_info), 100) + \
                    '{} suboptimal solutions\n\n'.format(num_suboptimal)
    truncated_readme += progress_line

    table = '| File   | Running Time |\n' \
            '| :----- | :----------- |\n'
    for line in progress_info:
        if line['time'] > 60:
            table += '| {} | **{}s** |\n'.format(line['file'], line['time'])
        elif line['time'] > 30:
            table += '| {} | *{}s* |\n'.format(line['file'], line['time'])
        else:
            table += '| {} | {}s |\n'.format(line['file'], line['time'])

    truncated_readme += table
    writable_readme = open('README.md', 'w')
    writable_readme.write(truncated_readme)
    print(truncated_readme)


execution_info = []
for solution in solutions_files:
    time_started = datetime.now()
    try:
        return_value = call(['python', solution])
    except SystemExit as e:
        pass
    time_finished = datetime.now()
    elapsed_seconds = (time_finished - time_started).total_seconds()
    info = {
        'file': solution,
        'time': elapsed_seconds
    }
    execution_info.append(info)
    print(info)

write_progress_table(execution_info)
