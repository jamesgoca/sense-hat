# get_commits = requests.get("https://api.github.com/repos/jamesgoca/site-calculator/commits")

# commits = get_commits.json()

for c in commits:
	if commit_total < 5:
		individual_commit = requests.get("https://api.github.com/repos/jamesgoca/site-calculator/commits/{}".format(c["sha"]))
		as_json = individual_commit.json()

		all_commits.append(as_json["stats"])
		commit_total += 1

for a in all_commits:
	if int(a["additions"]) > 10:
		pixel_matrix.append([255, 255, 255])
	else:
		pixel_matrix.append([0, 0, 0])