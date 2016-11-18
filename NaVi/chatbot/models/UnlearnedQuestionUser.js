'use strict';
const
    mongoose = require('mongoose'),
    Schema = mongoose.Schema;

var UnlearnedQuestionUser = new Schema({
    facebookId: {
        type: String,
        require: true,
        unique: true
    },
    unlearnedQuestions: [{
        _id: false,
        questionId: {
            type: Schema.Types.ObjectId,
            ref: 'Question'
        }
    }]
}, {
    timestamps: false,
    versionKey: false
});

module.exports = mongoose.model('UnlearnedQuestionUser', UnlearnedQuestionUser);