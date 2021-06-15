//
//  ViewController.swift
//  RPExt
//
//  Created by RenukaPa on 06/15/2021.
//  Copyright (c) 2021 RenukaPa. All rights reserved.
//

import UIKit
import RPExt

class ViewController: UIViewController {
    @IBOutlet weak var customImgView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        customImgView.circleImageView(borderColor: .red, borderWidth: 2.0)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

}

