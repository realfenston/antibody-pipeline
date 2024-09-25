# python simulatePDB.py
from openmm.app import *
from openmm import *
from openmm.unit import *
from sys import stdout
# 导入pdb文件
# 导入PDBx/mmCIF文件 使用PDBxFILE
pdb = PDBFile('input.pdb')
# 导入力场参数
# 文件名使用单引号
forcefield = ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
# 创建生物大分子体系 
# PME 长程电荷截断 截断 1nm (1*nanometer==10*angstrom) 氢键限制
system = forcefield.createSystem(pdb.topology, nonbondedMethod=PME,
        nonbondedCutoff=1*nanometer, constraints=HBonds)
# 积分器
# 模拟温度 交换系数 步长
# 如果模拟恒定能量体系，使用VerletIntegrator
integrator = LangevinMiddleIntegrator(300*kelvin, 1/picosecond, 0.004*picoseconds)
# 设置模拟
simulation = Simulation(pdb.topology, system, integrator)
# 指定初始原子坐标
simulation.context.setPositions(pdb.positions)
# 能量最小化
simulation.minimizeEnergy()
# 每1000步保存帧
simulation.reporters.append(PDBReporter('output.pdb', 1000))
# 每1000步保存运行状态
simulation.reporters.append(StateDataReporter(stdout, 1000, step=True,
        potentialEnergy=True, temperature=True))
# 运行步数
simulation.step(10000)
