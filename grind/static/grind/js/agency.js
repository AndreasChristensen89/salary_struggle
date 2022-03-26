var number = 0;
var order = 1;

document.addEventListener('DOMContentLoaded', function () {
    $('#next-hint').click(nextHint);
    $(".hint-btn").click(function(){
            number = $(this).attr("value");
            $("#introInterview").removeClass("d-none");
            $('#bubble-agency').css('opacity', '1');
            $('#bubble-agency').text(hrIntro[number][order]);
            $("#hint-row").addClass("d-none");
            $('#next-hint').removeClass("d-none");
            $("#next-hint").delay(2000).animate({opacity: "1.0"}, "fast");
        });
});

function nextHint() {
    order++;
    $('#bubble-agency').text(hrIntro[number][order]);

    if (!hrIntro[number][order]) {
        $('#next-hint').addClass("d-none");
        $("#introInterview").addClass("d-none");
        $('#interviewLink').removeClass("d-none");
        order = 1;
    }
}

const hrIntro = [{
    1: "Hi, I'm Steve the recruiter.",
    2: "Glad to meet you. You look like you have some promise.",
    3: "I'm pleased to let you know that your first interview is now available.",
    4: "I should probably give you a briefing of what you're about to join",
    5: "So, the company's name is Data Drifters and they specialize in database integrations.",
    6: "I'm not sure who will interview you.",
    7: "Also, you should know that interviewers are quite different from one another.",
    8: "They can be quite selfish.",
    9: "You basically have to adapt your answers to their personality traits in order to succeed.",
    10: "See if you can reach the impress level needed.",
    11: "Best of luck to you!",
  },
  {
    1: "Glad to hear the HR interview went well",
    2: "Next up is your coding interview.",
    3: "If you haven't studied for this one you might have some hardships",
    4: "Don't worry too much.",
    5: "There's always a chance that you can bluff your way out of a situation.",
    6: "Unfortunately for this one there's often only one correct answer...",
    7: "... unless you're able to convince the interviewer otherwise",
    8: "You can use your skills to benefit you.",
    9: "However, you will be penalized if the skill fails.",
    10: "Oh, by the way. I heard that the programming language will be Python.",
    11: "Better prepare a bit.",
    12: "Best of luck to you!",
  },
  {
    1: "I just heard the news. Great job on that coding interview!",
    2: "Your next interview is now available",
    3: "It'll be slightly harder since there is a time limit this time around.",
    4: "This one can be a bit unpredictable.",
    5: "It's hard for me to give you a whole lot of tips for it",
    6: "You'll see what I mean once you're there.",
    7: "Skill up and prepare the best you can.",
    8: "Give it your best shot!",
  },
  {
    1: "Wow! You actually managed to pass the interview.",
    2: "I know the guy... he can be a tool.",
    3: "Well, I suppose I can only congratulate you on making it this far.",
    4: "The final interview is now available.",
    5: "You'll be meeting the big boss. A wild guy to say the least.",
    6: "He'll probably try to scare you by bringing you in his dungeon-like office.",
    7: "Try to keep your cool. The job is within range.",
    8: "If you made it this far you have what it takes...",
    9: "... I'm pretty sure at least!",
    10: "Don't be discouraged! No fear! Go for glory!",
    11: "As always, I wish you the best of luck!",
    },
];
