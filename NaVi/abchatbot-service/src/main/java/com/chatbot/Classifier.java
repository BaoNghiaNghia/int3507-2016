package com.chatbot;

import com.maxent.DomainClassifier;
import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;

/**
 * Created by trieudh on 28/09/2016.
 */
public class Classifier {
    private String classLabel = "";
    private DomainClassifier domainClassifier = new DomainClassifier(System.getProperty("user.dir") + "/data/");

    String classify(String userMessage) {
        domainClassifier.init();
        this.classLabel = domainClassifier.doClassification(userMessage);
        return this.classLabel;
    }

    @Override
    public String toString() {
        try {
            return new JSONObject().put("intentClass", this.classLabel).toString();
        }
        catch (JSONException e) {
            return null;
        }
    }
}
