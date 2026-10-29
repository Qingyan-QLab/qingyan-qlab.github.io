"""Generate the original mathematical illustration; requires Python 3 only."""
from math import sin, cos, pi
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def point(u, v):
    radius = 140 + 57 * cos(v)
    x, y, z = radius * cos(u), radius * sin(u), 57 * sin(v)
    # Fixed camera for a slanted, sculptural view of the torus.
    a, b = 0.90, -0.50
    y, z = y * cos(a) - z * sin(a), y * sin(a) + z * cos(a)
    x, y = x * cos(b) - y * sin(b), x * sin(b) + y * cos(b)
    return x * 1.48 + 341, y * 1.48 + 299, z

parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 620" fill="none">',
         '<title>Q-lab — a study of form</title>',
         '<g stroke="#d8d9ce" stroke-width=".7"><path d="M47 299H633M341 50V548" stroke-dasharray="3 7"/><circle cx="341" cy="299" r="245" stroke-dasharray="2 7"/><path d="M45 46v13m-6-6h13M626 46v13m-6-6h13M45 543v13m-6-6h13M626 543v13m-6-6h13"/></g>',
         '<ellipse cx="341" cy="320" rx="305" ry="91" transform="rotate(-34 341 320)" stroke="#ba4b2b" stroke-opacity=".5" stroke-width=".9"/>']
faces = []
nu, nv = 100, 28
for i in range(nu):
    for j in range(nv):
        vertices = [point((i+du)*2*pi/nu, (j+dv)*2*pi/nv) for du,dv in [(0,0),(1,0),(1,1),(0,1)]]
        depth = sum(p[2] for p in vertices)/4
        shade = int(239 - 11 * (depth + 180)/360)
        fill = f'rgb({shade},{shade+1},{shade-9})'
        poly = ' '.join(f'{x:.2f},{y:.2f}' for x,y,_ in vertices)
        faces.append((depth,f'<polygon points="{poly}" fill="{fill}" stroke="#52694d" stroke-width=".55" stroke-opacity=".65" stroke-linejoin="round"/>'))
parts.extend(face for _,face in sorted(faces))
parts.extend(['<path d="M528 166C592 148 612 155 607 181" stroke="#ba4b2b" stroke-width=".9" stroke-opacity=".6"/>',
              '<circle cx="583" cy="204" r="7" fill="#bb4b2a"/><circle cx="583" cy="204" r="14" stroke="#bb4b2a" stroke-opacity=".25"/>',
              '<g font-family="monospace" font-size="9" letter-spacing="1.2" fill="#7f887a"><text x="51" y="290">Y</text><text x="349" y="64">Z</text><text x="614" y="315">X</text></g>', '</svg>'])
(ROOT/'assets'/'manifold.svg').write_text('\n'.join(parts))
print('Generated assets/manifold.svg')
