"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "h",
            "answer": "Hello, world!"
        },
        {
            "input": "q",
            "answer": "q"
        },
        {
            "input": "9",
            "answer": "99 bottles of beer on the wall,\n99 bottles of beer.\nTake one down, pass it around,\n98 bottles of beer on the wall.\n98 bottles of beer on the wall,\n98 bottles of beer.\nTake one down, pass it around,\n97 bottles of beer on the wall.\n97 bottles of beer on the wall,\n97 bottles of beer.\nTake one down, pass it around,\n96 bottles of beer on the wall.\n96 bottles of beer on the wall,\n96 bottles of beer.\nTake one down, pass it around,\n95 bottles of beer on the wall.\n95 bottles of beer on the wall,\n95 bottles of beer.\nTake one down, pass it around,\n94 bottles of beer on the wall.\n94 bottles of beer on the wall,\n94 bottles of beer.\nTake one down, pass it around,\n93 bottles of beer on the wall.\n93 bottles of beer on the wall,\n93 bottles of beer.\nTake one down, pass it around,\n92 bottles of beer on the wall.\n92 bottles of beer on the wall,\n92 bottles of beer.\nTake one down, pass it around,\n91 bottle of beer on the wall.\n91 bottle of beer on the wall,\n91 bottle of beer.\nTake one down, pass it around,\n9No bottles of beer on the wall.\n9No bottles of beer on the wall,\n9No bottles of beer.\nTake one down, pass it around,\n89 bottles of beer on the wall.\n89 bottles of beer on the wall,\n89 bottles of beer.\nTake one down, pass it around,\n88 bottles of beer on the wall.\n88 bottles of beer on the wall,\n88 bottles of beer.\nTake one down, pass it around,\n87 bottles of beer on the wall.\n87 bottles of beer on the wall,\n87 bottles of beer.\nTake one down, pass it around,\n86 bottles of beer on the wall.\n86 bottles of beer on the wall,\n86 bottles of beer.\nTake one down, pass it around,\n85 bottles of beer on the wall.\n85 bottles of beer on the wall,\n85 bottles of beer.\nTake one down, pass it around,\n84 bottles of beer on the wall.\n84 bottles of beer on the wall,\n84 bottles of beer.\nTake one down, pass it around,\n83 bottles of beer on the wall.\n83 bottles of beer on the wall,\n83 bottles of beer.\nTake one down, pass it around,\n82 bottles of beer on the wall.\n82 bottles of beer on the wall,\n82 bottles of beer.\nTake one down, pass it around,\n81 bottle of beer on the wall.\n81 bottle of beer on the wall,\n81 bottle of beer.\nTake one down, pass it around,\n8No bottles of beer on the wall.\n8No bottles of beer on the wall,\n8No bottles of beer.\nTake one down, pass it around,\n79 bottles of beer on the wall.\n79 bottles of beer on the wall,\n79 bottles of beer.\nTake one down, pass it around,\n78 bottles of beer on the wall.\n78 bottles of beer on the wall,\n78 bottles of beer.\nTake one down, pass it around,\n77 bottles of beer on the wall.\n77 bottles of beer on the wall,\n77 bottles of beer.\nTake one down, pass it around,\n76 bottles of beer on the wall.\n76 bottles of beer on the wall,\n76 bottles of beer.\nTake one down, pass it around,\n75 bottles of beer on the wall.\n75 bottles of beer on the wall,\n75 bottles of beer.\nTake one down, pass it around,\n74 bottles of beer on the wall.\n74 bottles of beer on the wall,\n74 bottles of beer.\nTake one down, pass it around,\n73 bottles of beer on the wall.\n73 bottles of beer on the wall,\n73 bottles of beer.\nTake one down, pass it around,\n72 bottles of beer on the wall.\n72 bottles of beer on the wall,\n72 bottles of beer.\nTake one down, pass it around,\n71 bottle of beer on the wall.\n71 bottle of beer on the wall,\n71 bottle of beer.\nTake one down, pass it around,\n7No bottles of beer on the wall.\n7No bottles of beer on the wall,\n7No bottles of beer.\nTake one down, pass it around,\n69 bottles of beer on the wall.\n69 bottles of beer on the wall,\n69 bottles of beer.\nTake one down, pass it around,\n68 bottles of beer on the wall.\n68 bottles of beer on the wall,\n68 bottles of beer.\nTake one down, pass it around,\n67 bottles of beer on the wall.\n67 bottles of beer on the wall,\n67 bottles of beer.\nTake one down, pass it around,\n66 bottles of beer on the wall.\n66 bottles of beer on the wall,\n66 bottles of beer.\nTake one down, pass it around,\n65 bottles of beer on the wall.\n65 bottles of beer on the wall,\n65 bottles of beer.\nTake one down, pass it around,\n64 bottles of beer on the wall.\n64 bottles of beer on the wall,\n64 bottles of beer.\nTake one down, pass it around,\n63 bottles of beer on the wall.\n63 bottles of beer on the wall,\n63 bottles of beer.\nTake one down, pass it around,\n62 bottles of beer on the wall.\n62 bottles of beer on the wall,\n62 bottles of beer.\nTake one down, pass it around,\n61 bottle of beer on the wall.\n61 bottle of beer on the wall,\n61 bottle of beer.\nTake one down, pass it around,\n6No bottles of beer on the wall.\n6No bottles of beer on the wall,\n6No bottles of beer.\nTake one down, pass it around,\n59 bottles of beer on the wall.\n59 bottles of beer on the wall,\n59 bottles of beer.\nTake one down, pass it around,\n58 bottles of beer on the wall.\n58 bottles of beer on the wall,\n58 bottles of beer.\nTake one down, pass it around,\n57 bottles of beer on the wall.\n57 bottles of beer on the wall,\n57 bottles of beer.\nTake one down, pass it around,\n56 bottles of beer on the wall.\n56 bottles of beer on the wall,\n56 bottles of beer.\nTake one down, pass it around,\n55 bottles of beer on the wall.\n55 bottles of beer on the wall,\n55 bottles of beer.\nTake one down, pass it around,\n54 bottles of beer on the wall.\n54 bottles of beer on the wall,\n54 bottles of beer.\nTake one down, pass it around,\n53 bottles of beer on the wall.\n53 bottles of beer on the wall,\n53 bottles of beer.\nTake one down, pass it around,\n52 bottles of beer on the wall.\n52 bottles of beer on the wall,\n52 bottles of beer.\nTake one down, pass it around,\n51 bottle of beer on the wall.\n51 bottle of beer on the wall,\n51 bottle of beer.\nTake one down, pass it around,\n5No bottles of beer on the wall.\n5No bottles of beer on the wall,\n5No bottles of beer.\nTake one down, pass it around,\n49 bottles of beer on the wall.\n49 bottles of beer on the wall,\n49 bottles of beer.\nTake one down, pass it around,\n48 bottles of beer on the wall.\n48 bottles of beer on the wall,\n48 bottles of beer.\nTake one down, pass it around,\n47 bottles of beer on the wall.\n47 bottles of beer on the wall,\n47 bottles of beer.\nTake one down, pass it around,\n46 bottles of beer on the wall.\n46 bottles of beer on the wall,\n46 bottles of beer.\nTake one down, pass it around,\n45 bottles of beer on the wall.\n45 bottles of beer on the wall,\n45 bottles of beer.\nTake one down, pass it around,\n44 bottles of beer on the wall.\n44 bottles of beer on the wall,\n44 bottles of beer.\nTake one down, pass it around,\n43 bottles of beer on the wall.\n43 bottles of beer on the wall,\n43 bottles of beer.\nTake one down, pass it around,\n42 bottles of beer on the wall.\n42 bottles of beer on the wall,\n42 bottles of beer.\nTake one down, pass it around,\n41 bottle of beer on the wall.\n41 bottle of beer on the wall,\n41 bottle of beer.\nTake one down, pass it around,\n4No bottles of beer on the wall.\n4No bottles of beer on the wall,\n4No bottles of beer.\nTake one down, pass it around,\n39 bottles of beer on the wall.\n39 bottles of beer on the wall,\n39 bottles of beer.\nTake one down, pass it around,\n38 bottles of beer on the wall.\n38 bottles of beer on the wall,\n38 bottles of beer.\nTake one down, pass it around,\n37 bottles of beer on the wall.\n37 bottles of beer on the wall,\n37 bottles of beer.\nTake one down, pass it around,\n36 bottles of beer on the wall.\n36 bottles of beer on the wall,\n36 bottles of beer.\nTake one down, pass it around,\n35 bottles of beer on the wall.\n35 bottles of beer on the wall,\n35 bottles of beer.\nTake one down, pass it around,\n34 bottles of beer on the wall.\n34 bottles of beer on the wall,\n34 bottles of beer.\nTake one down, pass it around,\n33 bottles of beer on the wall.\n33 bottles of beer on the wall,\n33 bottles of beer.\nTake one down, pass it around,\n32 bottles of beer on the wall.\n32 bottles of beer on the wall,\n32 bottles of beer.\nTake one down, pass it around,\n31 bottle of beer on the wall.\n31 bottle of beer on the wall,\n31 bottle of beer.\nTake one down, pass it around,\n3No bottles of beer on the wall.\n3No bottles of beer on the wall,\n3No bottles of beer.\nTake one down, pass it around,\n29 bottles of beer on the wall.\n29 bottles of beer on the wall,\n29 bottles of beer.\nTake one down, pass it around,\n28 bottles of beer on the wall.\n28 bottles of beer on the wall,\n28 bottles of beer.\nTake one down, pass it around,\n27 bottles of beer on the wall.\n27 bottles of beer on the wall,\n27 bottles of beer.\nTake one down, pass it around,\n26 bottles of beer on the wall.\n26 bottles of beer on the wall,\n26 bottles of beer.\nTake one down, pass it around,\n25 bottles of beer on the wall.\n25 bottles of beer on the wall,\n25 bottles of beer.\nTake one down, pass it around,\n24 bottles of beer on the wall.\n24 bottles of beer on the wall,\n24 bottles of beer.\nTake one down, pass it around,\n23 bottles of beer on the wall.\n23 bottles of beer on the wall,\n23 bottles of beer.\nTake one down, pass it around,\n22 bottles of beer on the wall.\n22 bottles of beer on the wall,\n22 bottles of beer.\nTake one down, pass it around,\n21 bottle of beer on the wall.\n21 bottle of beer on the wall,\n21 bottle of beer.\nTake one down, pass it around,\n2No bottles of beer on the wall.\n2No bottles of beer on the wall,\n2No bottles of beer.\nTake one down, pass it around,\n19 bottles of beer on the wall.\n19 bottles of beer on the wall,\n19 bottles of beer.\nTake one down, pass it around,\n18 bottles of beer on the wall.\n18 bottles of beer on the wall,\n18 bottles of beer.\nTake one down, pass it around,\n17 bottles of beer on the wall.\n17 bottles of beer on the wall,\n17 bottles of beer.\nTake one down, pass it around,\n16 bottles of beer on the wall.\n16 bottles of beer on the wall,\n16 bottles of beer.\nTake one down, pass it around,\n15 bottles of beer on the wall.\n15 bottles of beer on the wall,\n15 bottles of beer.\nTake one down, pass it around,\n14 bottles of beer on the wall.\n14 bottles of beer on the wall,\n14 bottles of beer.\nTake one down, pass it around,\n13 bottles of beer on the wall.\n13 bottles of beer on the wall,\n13 bottles of beer.\nTake one down, pass it around,\n12 bottles of beer on the wall.\n12 bottles of beer on the wall,\n12 bottles of beer.\nTake one down, pass it around,\n11 bottle of beer on the wall.\n11 bottle of beer on the wall,\n11 bottle of beer.\nTake one down, pass it around,\n1No bottles of beer on the wall.\n1No bottles of beer on the wall,\n1No bottles of beer.\nTake one down, pass it around,\n9 bottles of beer on the wall.\n9 bottles of beer on the wall,\n9 bottles of beer.\nTake one down, pass it around,\n8 bottles of beer on the wall.\n8 bottles of beer on the wall,\n8 bottles of beer.\nTake one down, pass it around,\n7 bottles of beer on the wall.\n7 bottles of beer on the wall,\n7 bottles of beer.\nTake one down, pass it around,\n6 bottles of beer on the wall.\n6 bottles of beer on the wall,\n6 bottles of beer.\nTake one down, pass it around,\n5 bottles of beer on the wall.\n5 bottles of beer on the wall,\n5 bottles of beer.\nTake one down, pass it around,\n4 bottles of beer on the wall.\n4 bottles of beer on the wall,\n4 bottles of beer.\nTake one down, pass it around,\n3 bottles of beer on the wall.\n3 bottles of beer on the wall,\n3 bottles of beer.\nTake one down, pass it around,\n2 bottles of beer on the wall.\n2 bottles of beer on the wall,\n2 bottles of beer.\nTake one down, pass it around,\n1 bottle of beer on the wall.\n1 bottle of beer on the wall,\n1 bottle of beer.\nTake one down, pass it around,\nNo bottles of beer on the wall."        },
        {
            "input": "+",
            "answer": ""
        }
    ],
    "Repetitions": [
        {
            "input": "hhhh",
            "answer": "Hello, world!\nHello, world!\nHello, world!\nHello, world!"
        },
        {
            "input": "qqqq"",
            "answer": "qqqq\nqqqq\nqqqq\nqqqq"
        },
        {
            "input": "++++"",
            "answer": ""
        }
    ],
    "Extra": [
        {
            "input": "hq9+",
            "answer": "Hello, world!\nhq9+99 bottles of beer on the wall,\n99 bottles of beer.\nTake one down, pass it around,\n98 bottles of beer on the wall.\n98 bottles of beer on the wall,\n98 bottles of beer.\nTake one down, pass it around,\n97 bottles of beer on the wall.\n97 bottles of beer on the wall,\n97 bottles of beer.\nTake one down, pass it around,\n96 bottles of beer on the wall.\n96 bottles of beer on the wall,\n96 bottles of beer.\nTake one down, pass it around,\n95 bottles of beer on the wall.\n95 bottles of beer on the wall,\n95 bottles of beer.\nTake one down, pass it around,\n94 bottles of beer on the wall.\n94 bottles of beer on the wall,\n94 bottles of beer.\nTake one down, pass it around,\n93 bottles of beer on the wall.\n93 bottles of beer on the wall,\n93 bottles of beer.\nTake one down, pass it around,\n92 bottles of beer on the wall.\n92 bottles of beer on the wall,\n92 bottles of beer.\nTake one down, pass it around,\n91 bottle of beer on the wall.\n91 bottle of beer on the wall,\n91 bottle of beer.\nTake one down, pass it around,\n9No bottles of beer on the wall.\n9No bottles of beer on the wall,\n9No bottles of beer.\nTake one down, pass it around,\n89 bottles of beer on the wall.\n89 bottles of beer on the wall,\n89 bottles of beer.\nTake one down, pass it around,\n88 bottles of beer on the wall.\n88 bottles of beer on the wall,\n88 bottles of beer.\nTake one down, pass it around,\n87 bottles of beer on the wall.\n87 bottles of beer on the wall,\n87 bottles of beer.\nTake one down, pass it around,\n86 bottles of beer on the wall.\n86 bottles of beer on the wall,\n86 bottles of beer.\nTake one down, pass it around,\n85 bottles of beer on the wall.\n85 bottles of beer on the wall,\n85 bottles of beer.\nTake one down, pass it around,\n84 bottles of beer on the wall.\n84 bottles of beer on the wall,\n84 bottles of beer.\nTake one down, pass it around,\n83 bottles of beer on the wall.\n83 bottles of beer on the wall,\n83 bottles of beer.\nTake one down, pass it around,\n82 bottles of beer on the wall.\n82 bottles of beer on the wall,\n82 bottles of beer.\nTake one down, pass it around,\n81 bottle of beer on the wall.\n81 bottle of beer on the wall,\n81 bottle of beer.\nTake one down, pass it around,\n8No bottles of beer on the wall.\n8No bottles of beer on the wall,\n8No bottles of beer.\nTake one down, pass it around,\n79 bottles of beer on the wall.\n79 bottles of beer on the wall,\n79 bottles of beer.\nTake one down, pass it around,\n78 bottles of beer on the wall.\n78 bottles of beer on the wall,\n78 bottles of beer.\nTake one down, pass it around,\n77 bottles of beer on the wall.\n77 bottles of beer on the wall,\n77 bottles of beer.\nTake one down, pass it around,\n76 bottles of beer on the wall.\n76 bottles of beer on the wall,\n76 bottles of beer.\nTake one down, pass it around,\n75 bottles of beer on the wall.\n75 bottles of beer on the wall,\n75 bottles of beer.\nTake one down, pass it around,\n74 bottles of beer on the wall.\n74 bottles of beer on the wall,\n74 bottles of beer.\nTake one down, pass it around,\n73 bottles of beer on the wall.\n73 bottles of beer on the wall,\n73 bottles of beer.\nTake one down, pass it around,\n72 bottles of beer on the wall.\n72 bottles of beer on the wall,\n72 bottles of beer.\nTake one down, pass it around,\n71 bottle of beer on the wall.\n71 bottle of beer on the wall,\n71 bottle of beer.\nTake one down, pass it around,\n7No bottles of beer on the wall.\n7No bottles of beer on the wall,\n7No bottles of beer.\nTake one down, pass it around,\n69 bottles of beer on the wall.\n69 bottles of beer on the wall,\n69 bottles of beer.\nTake one down, pass it around,\n68 bottles of beer on the wall.\n68 bottles of beer on the wall,\n68 bottles of beer.\nTake one down, pass it around,\n67 bottles of beer on the wall.\n67 bottles of beer on the wall,\n67 bottles of beer.\nTake one down, pass it around,\n66 bottles of beer on the wall.\n66 bottles of beer on the wall,\n66 bottles of beer.\nTake one down, pass it around,\n65 bottles of beer on the wall.\n65 bottles of beer on the wall,\n65 bottles of beer.\nTake one down, pass it around,\n64 bottles of beer on the wall.\n64 bottles of beer on the wall,\n64 bottles of beer.\nTake one down, pass it around,\n63 bottles of beer on the wall.\n63 bottles of beer on the wall,\n63 bottles of beer.\nTake one down, pass it around,\n62 bottles of beer on the wall.\n62 bottles of beer on the wall,\n62 bottles of beer.\nTake one down, pass it around,\n61 bottle of beer on the wall.\n61 bottle of beer on the wall,\n61 bottle of beer.\nTake one down, pass it around,\n6No bottles of beer on the wall.\n6No bottles of beer on the wall,\n6No bottles of beer.\nTake one down, pass it around,\n59 bottles of beer on the wall.\n59 bottles of beer on the wall,\n59 bottles of beer.\nTake one down, pass it around,\n58 bottles of beer on the wall.\n58 bottles of beer on the wall,\n58 bottles of beer.\nTake one down, pass it around,\n57 bottles of beer on the wall.\n57 bottles of beer on the wall,\n57 bottles of beer.\nTake one down, pass it around,\n56 bottles of beer on the wall.\n56 bottles of beer on the wall,\n56 bottles of beer.\nTake one down, pass it around,\n55 bottles of beer on the wall.\n55 bottles of beer on the wall,\n55 bottles of beer.\nTake one down, pass it around,\n54 bottles of beer on the wall.\n54 bottles of beer on the wall,\n54 bottles of beer.\nTake one down, pass it around,\n53 bottles of beer on the wall.\n53 bottles of beer on the wall,\n53 bottles of beer.\nTake one down, pass it around,\n52 bottles of beer on the wall.\n52 bottles of beer on the wall,\n52 bottles of beer.\nTake one down, pass it around,\n51 bottle of beer on the wall.\n51 bottle of beer on the wall,\n51 bottle of beer.\nTake one down, pass it around,\n5No bottles of beer on the wall.\n5No bottles of beer on the wall,\n5No bottles of beer.\nTake one down, pass it around,\n49 bottles of beer on the wall.\n49 bottles of beer on the wall,\n49 bottles of beer.\nTake one down, pass it around,\n48 bottles of beer on the wall.\n48 bottles of beer on the wall,\n48 bottles of beer.\nTake one down, pass it around,\n47 bottles of beer on the wall.\n47 bottles of beer on the wall,\n47 bottles of beer.\nTake one down, pass it around,\n46 bottles of beer on the wall.\n46 bottles of beer on the wall,\n46 bottles of beer.\nTake one down, pass it around,\n45 bottles of beer on the wall.\n45 bottles of beer on the wall,\n45 bottles of beer.\nTake one down, pass it around,\n44 bottles of beer on the wall.\n44 bottles of beer on the wall,\n44 bottles of beer.\nTake one down, pass it around,\n43 bottles of beer on the wall.\n43 bottles of beer on the wall,\n43 bottles of beer.\nTake one down, pass it around,\n42 bottles of beer on the wall.\n42 bottles of beer on the wall,\n42 bottles of beer.\nTake one down, pass it around,\n41 bottle of beer on the wall.\n41 bottle of beer on the wall,\n41 bottle of beer.\nTake one down, pass it around,\n4No bottles of beer on the wall.\n4No bottles of beer on the wall,\n4No bottles of beer.\nTake one down, pass it around,\n39 bottles of beer on the wall.\n39 bottles of beer on the wall,\n39 bottles of beer.\nTake one down, pass it around,\n38 bottles of beer on the wall.\n38 bottles of beer on the wall,\n38 bottles of beer.\nTake one down, pass it around,\n37 bottles of beer on the wall.\n37 bottles of beer on the wall,\n37 bottles of beer.\nTake one down, pass it around,\n36 bottles of beer on the wall.\n36 bottles of beer on the wall,\n36 bottles of beer.\nTake one down, pass it around,\n35 bottles of beer on the wall.\n35 bottles of beer on the wall,\n35 bottles of beer.\nTake one down, pass it around,\n34 bottles of beer on the wall.\n34 bottles of beer on the wall,\n34 bottles of beer.\nTake one down, pass it around,\n33 bottles of beer on the wall.\n33 bottles of beer on the wall,\n33 bottles of beer.\nTake one down, pass it around,\n32 bottles of beer on the wall.\n32 bottles of beer on the wall,\n32 bottles of beer.\nTake one down, pass it around,\n31 bottle of beer on the wall.\n31 bottle of beer on the wall,\n31 bottle of beer.\nTake one down, pass it around,\n3No bottles of beer on the wall.\n3No bottles of beer on the wall,\n3No bottles of beer.\nTake one down, pass it around,\n29 bottles of beer on the wall.\n29 bottles of beer on the wall,\n29 bottles of beer.\nTake one down, pass it around,\n28 bottles of beer on the wall.\n28 bottles of beer on the wall,\n28 bottles of beer.\nTake one down, pass it around,\n27 bottles of beer on the wall.\n27 bottles of beer on the wall,\n27 bottles of beer.\nTake one down, pass it around,\n26 bottles of beer on the wall.\n26 bottles of beer on the wall,\n26 bottles of beer.\nTake one down, pass it around,\n25 bottles of beer on the wall.\n25 bottles of beer on the wall,\n25 bottles of beer.\nTake one down, pass it around,\n24 bottles of beer on the wall.\n24 bottles of beer on the wall,\n24 bottles of beer.\nTake one down, pass it around,\n23 bottles of beer on the wall.\n23 bottles of beer on the wall,\n23 bottles of beer.\nTake one down, pass it around,\n22 bottles of beer on the wall.\n22 bottles of beer on the wall,\n22 bottles of beer.\nTake one down, pass it around,\n21 bottle of beer on the wall.\n21 bottle of beer on the wall,\n21 bottle of beer.\nTake one down, pass it around,\n2No bottles of beer on the wall.\n2No bottles of beer on the wall,\n2No bottles of beer.\nTake one down, pass it around,\n19 bottles of beer on the wall.\n19 bottles of beer on the wall,\n19 bottles of beer.\nTake one down, pass it around,\n18 bottles of beer on the wall.\n18 bottles of beer on the wall,\n18 bottles of beer.\nTake one down, pass it around,\n17 bottles of beer on the wall.\n17 bottles of beer on the wall,\n17 bottles of beer.\nTake one down, pass it around,\n16 bottles of beer on the wall.\n16 bottles of beer on the wall,\n16 bottles of beer.\nTake one down, pass it around,\n15 bottles of beer on the wall.\n15 bottles of beer on the wall,\n15 bottles of beer.\nTake one down, pass it around,\n14 bottles of beer on the wall.\n14 bottles of beer on the wall,\n14 bottles of beer.\nTake one down, pass it around,\n13 bottles of beer on the wall.\n13 bottles of beer on the wall,\n13 bottles of beer.\nTake one down, pass it around,\n12 bottles of beer on the wall.\n12 bottles of beer on the wall,\n12 bottles of beer.\nTake one down, pass it around,\n11 bottle of beer on the wall.\n11 bottle of beer on the wall,\n11 bottle of beer.\nTake one down, pass it around,\n1No bottles of beer on the wall.\n1No bottles of beer on the wall,\n1No bottles of beer.\nTake one down, pass it around,\n9 bottles of beer on the wall.\n9 bottles of beer on the wall,\n9 bottles of beer.\nTake one down, pass it around,\n8 bottles of beer on the wall.\n8 bottles of beer on the wall,\n8 bottles of beer.\nTake one down, pass it around,\n7 bottles of beer on the wall.\n7 bottles of beer on the wall,\n7 bottles of beer.\nTake one down, pass it around,\n6 bottles of beer on the wall.\n6 bottles of beer on the wall,\n6 bottles of beer.\nTake one down, pass it around,\n5 bottles of beer on the wall.\n5 bottles of beer on the wall,\n5 bottles of beer.\nTake one down, pass it around,\n4 bottles of beer on the wall.\n4 bottles of beer on the wall,\n4 bottles of beer.\nTake one down, pass it around,\n3 bottles of beer on the wall.\n3 bottles of beer on the wall,\n3 bottles of beer.\nTake one down, pass it around,\n2 bottles of beer on the wall.\n2 bottles of beer on the wall,\n2 bottles of beer.\nTake one down, pass it around,\n1 bottle of beer on the wall.\n1 bottle of beer on the wall,\n1 bottle of beer.\nTake one down, pass it around,\nNo bottles of beer on the wall."
        },
        {
            "input": "+q+",
            "answer": "+q+"
        },
        {
            "input": "qhq"",
            "answer": "qhq\nHello, world!\nqhq"
        }
    ]
}