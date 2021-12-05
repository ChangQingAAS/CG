using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Car : MonoBehaviour
{
    public float steerAngle;//转弯的角度
    public float enginePower;//汽车引擎的能量
    public Vector3 centerOfMass;//重心
    public float brake;
    public Rigidbody rb;

 //   public float speed=0.5f;

    public WheelCollider[] wheels; // 用来存储所有的轮子碰撞器
    public Transform[] visualWheels; //所有可见的轮子

    void Start()
    {
        rb.centerOfMass=centerOfMass;
    }

    void Update()
    {
        for(int i = 0; i < wheels.Length; i++)
        {
            Vector3 pos;//坐标
            Quaternion rot;//旋转值
            wheels[i].GetWorldPose(out pos,out rot);//collider的世界坐标
            visualWheels[i].position = pos;
            visualWheels[i].rotation = rot;
        }

        float v = Input.GetAxis("Vertical");//垂直输入值，按↑键，值为1；按↓键，值为-1。
        float h = Input.GetAxis("Horizontal");//水平输入值


        if (Input.GetKey(KeyCode.Space))//空格键实现刹车
        {
            brake = 25000;
        }
        else
        {
            brake = 0;
        }
        
            wheels[0].motorTorque = v * enginePower;//在车轮上的电机力矩
            wheels[1].motorTorque = v * enginePower;

            wheels[2].steerAngle = h * steerAngle;
            wheels[3].steerAngle = h * steerAngle;

            wheels[0].brakeTorque = brake;
            wheels[1].brakeTorque = brake;
    }
}
