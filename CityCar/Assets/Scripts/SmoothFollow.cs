using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[AddComponentMenu("Camera-Control/Smooth Follow CSharp")]

public class SmoothFollow : MonoBehaviour
{
    /*
    实现相机平滑地绕y轴和高度的旋转。
    到目标的水平距离始终不变。

    使用Lerp函数进行平滑处理。
    平滑处理后的值应用于变换的位置。
    */

    // 目标
    public Transform target;
    // 在x-z平面上到目标的距离
    public float distance = 10.0f;
    // 高度
    public float height = 5.0f; 
    public float heightDamping = 2.0f;
    public float rotationDamping = 3.0f;

    void LateUpdate()
    {
        if (!target)
            return;

        // 计算当前旋转角度
        float wantedRotationAngle = target.eulerAngles.y;
        float wantedHeight = target.position.y + height;
        float currentRotationAngle = transform.eulerAngles.y;
        float currentHeight = transform.position.y;

        currentRotationAngle = Mathf.LerpAngle(currentRotationAngle, wantedRotationAngle, rotationDamping * Time.deltaTime);

        // 减低高度
        currentHeight = Mathf.Lerp(currentHeight, wantedHeight, heightDamping * Time.deltaTime);

        // 将角度转换为rotation
        Quaternion currentRotation = Quaternion.Euler(0, currentRotationAngle, 0);

        transform.position = target.position;
        transform.position -= currentRotation * Vector3.forward * distance;

        //设置camera的高度
        transform.position = new Vector3(transform.position.x, currentHeight, transform.position.z);

        // 一直跟随着目标
        transform.LookAt(target);
    }
}
