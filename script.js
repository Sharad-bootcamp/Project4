function predictOutcome() {
    // Your JavaScript code goes here
    var battingTeam = document.getElementById('battingTeam').value;
    var bowlingTeam = document.getElementById('bowlingTeam').value;
    var venue = document.getElementById('venue').value;
    var target = parseInt(document.getElementById('target').value);
    var score = parseInt(document.getElementById('score').value);
    var overs = parseInt(document.getElementById('overs').value);
    var wickets = parseInt(document.getElementById('wickets').value);

    // Predictions and output display
    if (score > target) {
        alert(battingTeam + " won the match");
    } else if (score === target - 1 && overs === 20) {
        alert("Match Drawn");
    } else if (wickets === 10 && score < target - 1) {
        alert(bowlingTeam + " won the match");
    } else if (battingTeam === bowlingTeam) {
        alert("To proceed, please select different teams as no match can be played between the same teams");
    } else {
        if (0 <= target && target <= 300 && 0 <= overs && overs <= 20 && 0 <= wickets && wickets <= 10 && 0 <= score) {
            try {
                var runsLeft = target - score;
                var ballsLeft = 120 - (overs * 6);
                var wicketsLeft = 10 - wickets;
                var currentRunRate = score / overs;
                var requiredRunRate = (runsLeft * 6) / ballsLeft;

                // Replace these lines with your actual prediction logic
                var winProbability = 0.7;
                var lossProbability = 0.3;

                // Display predictions using alert (for simplicity)
                alert(battingTeam + " - " + Math.round(winProbability * 100) + "%");
                alert(bowlingTeam + " - " + Math.round(lossProbability * 100) + "%");

            } catch (error) {
                alert("Please fill in all the required details");
            }
        } else {
            alert("There is something wrong with the input, please fill in the correct details as of IPL T-20 format");
        }
    }
}
