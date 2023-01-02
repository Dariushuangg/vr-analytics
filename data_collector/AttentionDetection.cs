using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.SceneManagement;

public class AttentionDetector : MonoBehaviour
{
    [SerializeField] private Transform headTransform;
    [SerializeField] private LayerMask AnalyticsLayer;

    // experiment data
    private int isomerCount;
    private int confusionCount;
    private int tableCount;
    private int UICount;
    private int totalFrameCount;

    private int correctGrabCount;
    private int confusionGrabCount;
    private int successCount;
    private int failureCount;

    private float x;
    private float y;
    private float z;
    private float alpha;
    private float beta;
    private float gamma;

    // parameters for saving files
    private string now;
    private string path;

    void OnEnable()
    {
        // Visual concentration variables
        isomerCount = confusionCount = tableCount = UICount = totalFrameCount = 0;
        // Outcome variables
        correctGrabCount = confusionGrabCount = successCount = failureCount = 0;
        // Head pose variables
        x = y = z = 0f;
        alpha = beta = gamma = 0f;
        now = System.DateTime.Now.ToString("yyyy-MM-dd_HH-mm-ss");
        CreateText(now);
    }

    void Update()
    {
        totalFrameCount += 1;

        RaycastHit hit;
        if (Physics.Raycast(headTransform.position, headTransform.forward, out hit, 100, Physics.AllLayers)) {
            string tag = hit.collider.gameObject.tag;

            switch (tag) {
                case "Isomer":
                    isomerCount += 1;
                    break;
                case "Confusion":
                    confusionCount += 1;
                    break;
                case "Table":
                    tableCount += 1;
                    break;
            }
        }

        RaycastHit UIHit;
        if (Physics.Raycast(headTransform.position, headTransform.forward, out UIHit, 100, AnalyticsLayer)) {
            UICount += 1;
        }

        x = gameObject.transform.position.x;
        y = gameObject.transform.position.y;
        z = gameObject.transform.position.z;
        alpha = gameObject.transform.rotation.eulerAngles.x;
        beta = gameObject.transform.rotation.eulerAngles.y;
        gamma = gameObject.transform.rotation.eulerAngles.z;

        WriteText();
    }

    private void testText() {
        GameObject obj0 = GameObject.FindGameObjectsWithTag("testtag")[0];
        obj0.GetComponent<TMPro.TextMeshProUGUI>().text = "isomerCount: " + isomerCount;

        GameObject obj1 = GameObject.FindGameObjectsWithTag("testtag1")[0];
        obj1.GetComponent<TMPro.TextMeshProUGUI>().text = "correctGrabCount: " + correctGrabCount;

        GameObject obj2 = GameObject.FindGameObjectsWithTag("testtag2")[0];
        obj2.GetComponent<TMPro.TextMeshProUGUI>().text = "tableCount: " + tableCount;

        GameObject obj3 = GameObject.FindGameObjectsWithTag("testtag3")[0];
        obj3.GetComponent<TMPro.TextMeshProUGUI>().text = "x: " + x;
    }

    void CreateText(string now) {
        path = Application.persistentDataPath + "/" + now + "_" + SceneManager.GetActiveScene().name + "_I3T.txt";

        if (!File.Exists(path))
        {
            File.WriteAllText(path, "time,isomer_view,confusor_view,table_view,UI_view,total_frame,isomer_grab,confusor_grab,success_count,failure_count,x,y,z,alpha,beta,gamma\n");
        }

        WriteText();
    }

    void WriteText() {
        string content = Time.time.ToString() + ","
        + isomerCount + ","
        + confusionCount + ","
        + tableCount + ","
        + UICount + ","
        + totalFrameCount + ","
        + correctGrabCount + ","
        + confusionGrabCount + ","
        + successCount + ","
        + failureCount + ","
        + x + ","
        + y + ","
        + z + ","
        + alpha + ","
        + beta + ","
        + gamma + "\n";

        File.AppendAllText(path, content);
    }

    public void CorrectGrabCountAdd() {
        correctGrabCount += 1;
    }

    public void ConfusionGrabCountAdd()
    {
        confusionGrabCount += 1;
    }

    public void successCountAdd()
    {
        successCount += 1;
    }


    public void failureCountAdd()
    {
        failureCount += 1;
    }

    void OnDisable()
    {
        string content = "0,0,0,0,0,0,0,0,"+ successCount +",0,0,0,0,0,0,0 \n";
        File.AppendAllText(path, content);
    }
}
