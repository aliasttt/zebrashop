
document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed");  // Debugging line
    var questions = document.querySelectorAll('p.question');
    questions.forEach(function(question) {
        question.addEventListener('click', function() {
            var answer = this.nextElementSibling;
            if (answer && answer.classList.contains('answer')) {
                if (answer.style.display === 'block' || answer.style.display === '') {
                    answer.style.display = 'none';
                } else {
                    answer.style.display = 'block';
                }
                console.log("Question clicked");  // Debugging line
            } else {
                console.error("Next sibling not found or not an answer:", answer);  // Debugging line
            }
        });
    });
});