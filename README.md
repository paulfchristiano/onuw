Usage: `python onuw.py player1,player2,...,playerN role1,role2,...,roleM [slack]`

E.g. `python onuw.py Alice,Bob,Charlie robber,apprenticeseer,seer,werewolf,dreamwolf,troublemaker`


Starts a game with the indicated players and roles.


The players should be listed in either clockwise or counterclockwise order
(for purpose of village idiot, and passing around computer)


If `slack` argument is present, deliver night messages over slack
for any players whose name is the first name of a user in the slack workspace 
(you need to follow instructions below to set it up)


All night actions are randomized.
This results in a few material changes to the game.
(Many decisions were basically random anyway):


  * Seer looks in middle 50% of the time
  * Witch takes suspicious roles for herself 50% of the time
  * PI and medium always look at first role, look at second role 50% of the time
  * Village idiot doesn't rotate 20% of the time
  * Troublemaker, robber, and witch always act
  * No one can make choices based on village idiot affecting nearby locations
  * Village idiot can't choose direction based on shield
  * Curator marks a revealed player with the same probability rate as other players
  * Doppelganger troublemaker switches troublemaker at same probability
  * Doppelganger revealer reveals the revealer at same probability
  * Doppelganger curator marks the curator at same probability
  * Doppelganger witch never switches the witch
  * Doppelganger robber never robs the robber
  * Doppelganger PI never looks at the PI


This app also implements some new roles:


  * Lucdiwolf: like dreamwolf but sees a center card
  * Medium: like PI but looks in the center
  * Fool: like drunk, but views two cards they didn't pick
  * Madseer: sees two players' roles. But one of them is made up randomly.
  * Loverwolf/Loverewerewolf: normal wolf or villager. Sees the other lovers. Is scored as if other lovers are on their team.
  * Merlin: sees all wolves. Villagers lose if all wolves vote for them.
  * Trickster: exchanges a random player's card with a random middle card. Doesn't learn which player or card, only which role.
  * Imposter: is seen as a werewolf.
  * God/enemy of reason: sees everything that happens. Do whatever you want with that.


Note that you can have multiple copies of a role, who will act in a random order.


Instructions to set up slack:

  * Go to `https://<slackdomain>.slack.com/apps/A0F7YS25R-bots`
  * Make a bot by clicking `Add Configuration`, and download the corresponding token
  * Create a new file slack_token.py in this directory, with the single line `slack_token = "..."`

