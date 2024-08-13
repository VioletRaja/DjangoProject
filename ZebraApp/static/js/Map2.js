
function updateRating() {
    let ratings = [
        { stars: 5, count: 7 },
        { stars: 4, count: 5 },
        { stars: 3, count: 3 },
        { stars: 2, count: 2 },
        { stars: 1, count: 0 }
    ];

    let totalStars = 0;
    let totalReviews = 0;

    ratings.forEach(item => {
        totalStars += item.stars * item.count;
        totalReviews += item.count;
    });

    let averageRating = totalReviews > 0 ? (totalStars / totalReviews).toFixed(1) : 0;

    document.getElementById('range5').style.width = `${(ratings[0].count / totalReviews) * 100}%`;
    document.getElementById('range4').style.width = `${(ratings[1].count / totalReviews) * 100}%`;
    document.getElementById('range3').style.width = `${(ratings[2].count / totalReviews) * 100}%`;
    document.getElementById('range2').style.width = `${(ratings[3].count / totalReviews) * 100}%`;
    document.getElementById('range1').style.width = `${(ratings[4].count / totalReviews) * 100}%`;

    document.getElementById('average').innerHTML = `<b>${averageRating}</b>`;
}

function submitReview() {
    let newReviewStars = 4;
    ratings[newReviewStars - 1].count++;

    updateRating();
}

document.addEventListener('DOMContentLoaded', function() {
    updateRating();
});




